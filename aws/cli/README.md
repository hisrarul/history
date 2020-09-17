#### Let's assume that you got a requirement to list all subdomain recordsets entries updated in hosted zone
##### Solution using shell script

```
for HOSTED_ZONE_ID in $(aws route53 list-hosted-zones | grep hostedzone | cut -d'/' -f3 | cut -d'"' -f1)  #Get the hosted zone ids
do
    echo ""
    echo Hosted zone: $HOSTED_ZONE_ID         #echo hosted zone
    aws route53 list-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID | grep -w Name | uniq | cut -d'"' -f4 | grep -v ^[0-9_] | grep -v domainkey        #filter out only valid domain urls
done
```

#### Create s3 bucket in region other than us-east-1
```aws s3api create-bucket --bucket kops-israrul --create-bucket-configuration LocationConstraint=ap-south-1```
