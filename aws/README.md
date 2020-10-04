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

#### References
* [1] [Console access from restricted IP address](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html)
* [2] [MFA mandatory for users](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.html)
