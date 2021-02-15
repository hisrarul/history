## EC2

#### Get list of instance ip addresses in a vpc
```
vpc_id=<enter_vpc_id>
aws ec2 describe-instances --filters Name=network-interface.vpc-id,Values=${vpc_id} --query 'Reservations[*].Instances[*].NetworkInterfaces[*].PrivateIpAddresses[*].PrivateIpAddress' --output text
```
