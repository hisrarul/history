import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Code, Function, LayerVersion, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Duration, RemovalPolicy, stringToCloudFormation } from 'aws-cdk-lib';
import { CODEPIPELINE_CROSS_ACCOUNT_KEY_ALIAS_STACK_SAFE_RESOURCE_NAME } from 'aws-cdk-lib/cx-api';
import { join } from 'path';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb';
import { LambdaIntegration, RestApi } from 'aws-cdk-lib/aws-apigateway';

export class ThumbnailServiceCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new Table(this, 'thumbnail-tbl', {
      partitionKey: {name: 'id', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const handler = new Function(this, 'handler-function-resizeImg', {
      runtime: Runtime.PYTHON_3_8,
      timeout: Duration.seconds(20),
      handler: 'app.s3_thumbnail_generator',
      code: Code.fromAsset(join(__dirname, '../lambdas')),
      layers: [
        LayerVersion.fromLayerVersionArn(
          this,
          "PIL",
          "arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p38-Pillow:5"
        )
      ],
      environment: {
        MY_TABLE: table.tableName,
        REGION_NAME: "us-east-1",
        THUMBNAIL_SIZE: "128"
      }
    });

    // grant permission for lambda to read and write table
    table.grantReadWriteData(handler)


    const handlerListThumbnails = new Function(this, 'handler-function-get-thumbnail-url', {
      runtime: Runtime.PYTHON_3_8,
      timeout: Duration.seconds(20),
      handler: 'app.s3_get_thumbnail_urls',
      memorySize: 512,
      code: Code.fromAsset(join(__dirname, '../lambdas')),
      layers: [
        LayerVersion.fromLayerVersionArn(
          this,
          "PIL-2",
          "arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p38-Pillow:5"
        )
      ],
      environment: {
        MY_TABLE: table.tableName,
        REGION_NAME: "us-east-1",
        THUMBNAIL_SIZE: "128"
      }
    });

    table.grantReadData(handlerListThumbnails)

    const s3Bucket = new s3.Bucket(this, 'photo-bucket', {
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true
    });

    s3Bucket.grantReadWrite(handler);

    s3Bucket.addEventNotification(s3.EventType.OBJECT_CREATED,
    new s3n.LambdaDestination(handler));

    handler.addToRolePolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        actions: ['s3:*'],
        resources: ['*']
      })
    )

    // Create rest api
    const thumbsApi = new RestApi(this, "thump-api", {
      description: "list all thumbnails and metadata"
    });

    // Lambda integration

    const handlerApiIntegration = new LambdaIntegration(handlerListThumbnails, 
      {requestTemplates: {"application/json": '{"statusCode": "200"}'}});

    const mainPath = thumbsApi.root.addResource("images");

    mainPath.addMethod("GET", handlerApiIntegration)

  }
}
