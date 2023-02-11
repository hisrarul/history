import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
import { join } from 'path';
import { Duration } from 'aws-cdk-lib';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';

export class CronCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const handlerFunction = new lambda.Function(this, 'CronQuote', {
      code: lambda.Code.fromAsset(join(__dirname, '../lambdas')),
      handler: 'app.handler',
      timeout: Duration.seconds(300),
      runtime: lambda.Runtime.PYTHON_3_9
    });

    const rule = new events.Rule(this, 'Cron-Rule', {
      schedule: events.Schedule.expression('cron(0 6 ? * MON-FRI *)'),
     });

     rule.addTarget(new targets.LambdaFunction(handlerFunction));
  }
}
