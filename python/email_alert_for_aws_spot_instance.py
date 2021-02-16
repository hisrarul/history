import boto3
import smtplib
from datetime import datetime

client = boto3.client('autoscaling',
                        aws_access_key_id='xxxxxxxxxxxxxxxxxx',
                        aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxx')

def getInstanceType(asgName):
    InstanceList = []
    # describe autoscaling group
    response = client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[
            asgName
        ],
        MaxRecords=1
    )
    # append instance types of autoscaling group in a list
    for Type in response['AutoScalingGroups'][0]['MixedInstancesPolicy']['LaunchTemplate']['Overrides']:
        InstanceList.append(Type['InstanceType'])
    return InstanceList

def sendEmail(asgName):
    # creates SMTP session 
    email = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # TLS for security 
    email.starttls() 
    
    # compiler gives an error for wrong credential. 
    email.login("<youremail@gmail.com>", "<your_password>") 
    
    # get instance type list
    instanceTypeList = getInstanceType(asgName)
    instanceCommaSeparatedItem = ', '.join(map(str, instanceTypeList))

    # message to be sent 
    message = "Subject: Email notification for AutoScaling Group \n\nThis is inform you that spot instance type {} is not available in auto scaling group '{}' at aws end.".format(instanceCommaSeparatedItem,asgName)
    
    # sending the mail 
    email.sendmail("<sender_email_address>", "<receiver_email_address>", message) 
    
    # terminating the session 
    email.quit()


def timeDifference(tsInAsgActivity):
    # get current time in utc format
    now = datetime.utcnow()
    
    # remove time zone from autoscaling group activity's output
    naive = tsInAsgActivity.replace(tzinfo=None)
    
    # calculate the difference in time between asg start timestamp and current utc time 
    tdelta = now - naive
    
    # convert time in minutes
    diffInMinutes = tdelta.total_seconds() / 60
    return diffInMinutes

def describeScalingActivitiesRequest(asgName):
    # describe autoscaling group activity
    response = client.describe_scaling_activities(
        AutoScalingGroupName=asgName,
        MaxRecords=1
    )
    # timestamp in autoscaling group activity
    tsInAsgActivity = response['Activities'][0]['StartTime']
    
    # check if time difference is greater than 2 mins
    if timeDifference(tsInAsgActivity) > 2:
        td = timeDifference(tsInAsgActivity)
        print('Email is not triggered because last activity in ASG is quite older: ' + str(td) + ' minutes.')
    else:
        # check if the spot instance is not available in asg activity and trigger email
        if 'UnfulfillableCapacity' in response['Activities'][0]['Description']:
            sendEmail(asgName)

# execute the function with auto scaling group
describeScalingActivitiesRequest('autoscaling-group-spot-instance')
