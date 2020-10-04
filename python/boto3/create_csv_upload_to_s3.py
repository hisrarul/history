import csv
import os
import boto3
import json

def lambda_handler(event, context):
    os.chdir('/tmp')
    with open('eggs.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


    client = boto3.client('s3')
    s3 = boto3.client('s3')


    with open('eggs.csv', 'rb') as data:
        s3.upload_fileobj(data, 'beback-demo-sep', 'eggs.csv')

    return {
        'body': json.dumps('Uploaded and we are testing local zip file!')
    }
