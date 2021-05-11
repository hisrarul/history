## Error

#### 1. com.amazonaws.services.s3.model.AmazonS3Exception: Status Code: 400, AWS Service: Amazon S3, AWS Request ID: 4324234KDNMY, AWS Error Code: null, AWS Error Message: Bad Request, S3 Extended Request ID: xzfsdkfjsdfuewrsdfdf059845hjsfdkdfgsd/Uggpasrewdd=\n'
b'\tat com.amazonaws.http.AmazonHttpClient.handleErrorResponse(AmazonHttpClient.java:798)\n'
b'\tat com.amazonaws.http.AmazonHttpClient.executeHelper(AmazonHttpClient.java:421)\n'
b'\tat com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:232)\n'
b'\tat com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:3528)\n'
b'\tat com.amazonaws.services.s3.AmazonS3Client.headBucket(AmazonS3Client.java:1031)\n'
b'\tat com.amazonaws.services.s3.AmazonS3Client.doesBucketExist(AmazonS3Client.java:994)\n'

Summary: Unable to read file from s3 bucket from spark job running on Airflow

```
Sol: Need to pass extra conf for s3
extra_conf = []
extra_conf.append("spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SharedInstanceProfileCredentialsProvider")
extra_conf.append("spark.hadoop.fs.s3a.endpoint=s3.us-east-1.amazonaws.com")
extra_conf.append("spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem")
extra_conf.append("spark.executor.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true")
extra_conf.append("spark.driver.extraJavaOptions=-Dcom.amazonaws.services.s3.enabledV4=true")
