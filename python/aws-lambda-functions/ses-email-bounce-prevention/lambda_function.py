import time
import boto3
import logging

dbName = 'bounceemail'
tableName = 'sesblog2'
sesEventType = 'Bounce'
output='s3://israr-test-result/'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def getIamUserListFromAthena():
    client = boto3.client('athena')
    query = "SELECT mail.tags.ses_caller_identity as User FROM {} WHERE eventType = \'{}\'".format(tableName,sesEventType)
    queryResult = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': dbName
        },
        ResultConfiguration={
            'OutputLocation': output,
        }
    )

    logging.info("Query result \n {}".format(queryResult))
    queryId = queryResult['QueryExecutionId']
    time.sleep(5)
    getQueryResult = client.get_query_results(
        QueryExecutionId=queryId
    )
    iamUsers=[]
    for row in getQueryResult['ResultSet']['Rows']:
        if row['Data'][0]['VarCharValue'] != 'User':
            sesUser = row['Data'][0]['VarCharValue']
            iamUsers.append(sesUser.split('"')[1])
            logging.info("List of IAM users: \"{}\"".format(iamUsers))
    return iamUsers

def getIamUserAccessId(iamUserNames):
    client = boto3.client('iam')
    userAndAccessDetails = {}
    for iamUser in iamUserNames:
        userAccessIdList = []
        paginator = client.get_paginator('list_access_keys')
        for userJsonData in paginator.paginate(UserName=iamUser):
            for akm in userJsonData['AccessKeyMetadata']:
                userAccessIdList.append(akm['AccessKeyId'])
        logger.info("User \"{}\" access id list \"{}\"".format(iamUser, userAccessIdList))
        userAndAccessDetails[iamUser] = userAccessIdList
    return userAndAccessDetails


def deactiveIamUser(iamUser, userAccessIds):
    iam = boto3.resource('iam')
    for userAccessId in userAccessIds:
        access_key = iam.AccessKey(iamUser,userAccessId)
        userDeactivationResult = access_key.deactivate()
        logger.info("User \"{}\" access id \"{}\" has been disabled.".format(iamUser,userAccessId))

def update_dynamoDB(iamUser, userAccessIds):    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('raghib_test')
    with table.batch_writer() as batch:
        for userAccessId in userAccessIds:
            batch.put_item(
                Item={
                    'IAM_User': iamUser,
                    'access_key': userAccessId
                }
            )
        logger.info("User \"{}\" access id \"{}\" has been disabled.".format(iamUser,userAccessId))

# def lambda_handler():
def lambda_handler(event, context):
    userList = getIamUserListFromAthena()
    usersAndKeys = getIamUserAccessId(userList)
    for user,keys in usersAndKeys.items():
        deactiveIamUser(user, keys)
    for user,keys in usersAndKeys.items():
        update_dynamoDB(user, keys)