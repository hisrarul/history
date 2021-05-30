## SES Email Bounce Prevention

### Create table for json data
```bash
CREATE EXTERNAL TABLE `bounceemaildb.eventsUserstb`(
  `eventtype` string COMMENT 'from deserializer', 
  `mail` struct<timestamp:string,
                source:string,
                sourcearn:string,
                sendingaccountid:string,
                messageid:string,
                destination:string,
                headerstruncated:boolean,
                headers:array<struct<name:string,value:string>>,
                commonheaders:struct<from:array<string>,to:array<string>,messageid:string,subject:string>,
                tags:struct<ses_configurationset:string,ses_source_ip:string,ses_from_domain:string,ses_caller_identity:string>> COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'mapping.ses_caller_identity'='ses:caller-identity', 
  'mapping.ses_configurationset'='ses:configuration-set', 
  'mapping.ses_from_domain'='ses:from-domain', 
  'mapping.ses_source_ip'='ses:source-ip') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://israr-test/'
TBLPROPERTIES (
  'transient_lastDdlTime'='1622303073')' 
```

### Steps for local testing:
```bash
pip install boto3 -t .
python lambda_function.py

# Note: Make sure that your provide access to aws service using aws cli or export access using env variables.
```

### To execute on AWS Lambda function
1. Create function lambda with role which has permission to the followings
    a. s3 read and write access
    b. athena access to query
    c. iam access to deactivate programmatic access
    4. cloudwatch access to log

Reference:

https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/