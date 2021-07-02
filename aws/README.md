### Restrict AWS console access to whitelisted IP address
* [Create IAM Policy](https://github.com/hisrarul/history/blob/master/aws/aws-console-restricted-from-vpn-ip.json) [1]
* Attach it to the user or group.
---

### Disable access of all resources if mfa device is not attached
* [Create IAM Policy](https://github.com/hisrarul/history/blob/master/aws/aws-iam-policy-mfa-compulsory.json) [2]
* Attach it to the user or group
---

### AWS region restriction
[Yet Not Tested](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html)

---

### Install AWS Cloudwatch Agent on Ubuntu OS
We are using system manager to login ec2 instances which needs cloudwatch agent to run on it.
* [Install Cloudwatch agent from userdata](https://github.com/hisrarul/history/blob/master/aws/install-aws-cloudwatch-agent.sh)
---

## Create csv file and upload to s3 bucket using python [AWS Lambda]
```
python ../python/boto3/create_csv_upload_to_s3.py
```
## Cross account s3 bucket
* [Cross account access s3](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)
* [Update s3 bucket permission](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.html)
```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "Example permissions",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::AccountB-ID:root"
         },
         "Action": [
            "s3:GetBucketLocation",
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::DOC-EXAMPLE-BUCKET"
         ]
      },
      {
         "Sid": "Deny permission",
         "Effect": "Deny",
         "Principal": {
            "AWS": "arn:aws:iam::AccountB-ID:root"
         },
         "Action": [
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::DOC-EXAMPLE-BUCKET"
         ]
      }
   ]
}
```

#### References
* [1] [Console access from restricted IP address](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html)
* [2] [MFA mandatory for users](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.html)
