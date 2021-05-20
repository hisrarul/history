#!/bin/bash

#Tried on AWS

END_DATE=$(date +%Y-%m-%d)
INST_TYPE='m4.xlarge'

RequestNumber = $(aws cloudwatch get-metric-statistics --namespace AWS/ApplicationELB --metric-name RequestCount --statistics Average  --period 3600 --dimensions Name=LoadBalancer,Value=app/demo/bee684fbe96d7c08 Name=TargetGroup,Value=targetgroup/tg/0bf32752ed9deb70 --start-time 2019-11-01T00:00:00Z --end-time "$END_DATE"T00:00:00Z --query Datapoints['Average'])


if test $RequestNumber -gt 5000
then
echo "Change the type of instance"
aws ec2 modify-instance-attribute --instance-id i-00000000 --instance-type "{\"Value\": \"$INST_TYPE\"}
fi