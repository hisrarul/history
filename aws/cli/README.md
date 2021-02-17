## Let's assume that you got a requirement to list all subdomain recordsets entries updated in hosted zone
[Route53 recordset](https://github.com/hisrarul/history/blob/master/aws/cli/list_recordsets_route53.md)

## Create s3 bucket in region other than us-east-1
```aws s3api create-bucket --bucket kops-israrul --create-bucket-configuration LocationConstraint=ap-south-1```

## Create IAM user with console access using cli
[IAM user](https://github.com/hisrarul/history/blob/master/aws/cli/create_aws_iam_user.md)


## Change owner of files in s3 bucket
This is generally required when try to copy objects from one s3 bucket of an account to another s3 bucket of another account.

#### Grant access during a put or copy operation
```
#source https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-owner-access/

aws s3api copy-object --bucket destination_DOC-EXAMPLE-BUCKET --key source_DOC-EXAMPLE-BUCKET/myobject --acl bucket-owner-full-control
-or-
aws s3 cp s3://source_DOC-EXAMPLE-BUCKET/myobject s3://destination_DOC-EXAMPLE-BUCKET/ --acl bucket-owner-full-control
```


#### Grant access after the object is added to the bucket
```
aws s3api put-object-acl --bucket destination_DOC-EXAMPLE-BUCKET --key keyname --acl bucket-owner-full-control
```
