from pywebhdfs.webhdfs import PyWebHdfsClient
from datetime import datetime
import time
import os
import logging
import internalEmail

# Define env variable and its values such as QA, Production
hdfsEnv = os.environ['HDFS_ON_ENV']
hdfsUrl = os.environ['HDFS_HOST_URL']
totalNumberOfsuccessfulCounts = os.environ['TOTAL_HEALTH_CHECK']
totalNumberOfFailedCounts = os.environ['TOTAL_HEALTH_CHECK']

# Set log level
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create temp file to test upload on hdfs
now = datetime.now()
logging_data = str(now) + " Last upload timestamp"
logging_alert_file = 'upload_stat.txt'

# Initialize object
hdfs = PyWebHdfsClient(host=hdfsUrl,port='50070')


# Delete logging_alert_file from hdfs
def delete_from_hdfs():
  try:
    hdfs.delete_file_dir(logging_alert_file)
  except Exception as e:
    print(e)


# Upload consecutive test and count
def upload_to_hdfs():

  try:
    successfulCount=failedCount=0
    while successfulCount < int(totalNumberOfsuccessfulCounts):
      successfulCount = successfulCount + 1 
      hdfs.create_file(logging_alert_file, logging_data)
      time.sleep(60)
    logger.info("File has been uploaded to HDFS {}".format(now))

  except Exception as e:
    if 'already exists' in str(e):
      logger.info("File: " + logging_alert_file + " already exist. Deleting for next run..")
      delete_from_hdfs()
    else:
      while failedCount < int(totalNumberOfFailedCounts):
        print(e)
        # Consecutive check for failed uploads in a interval of 60 sec
        time.sleep(60)
        failedCount = failedCount + 1
        logger.error('File upload failed count {}.'.format(failedCount))
      return failedCount


if upload_to_hdfs() == int(totalNumberOfFailedCounts):
  emailSubject = "Critical Alert in {} HDFS".format(hdfsEnv)
  emailBody = '<html><body><h2 style="color:red">{} HDFS on Alert</h2><h4>This is inform you that unable to upload file to {}. Consider this as temporary fail if you don\'t receive multiple alerts in next 10 mins.</h4><h5>Time: {}</h5><h3>Regards,<br>DevOps Team</h3></body></html>'.format(hdfsEnv,hdfsUrl, now)
  mail = internalEmail.internalemailalert(emailSubject,emailBody)
  recipients = mail.sendMail()
  print("Consecutive trail of file upload failed, Sending email alert to {}".format(recipients))