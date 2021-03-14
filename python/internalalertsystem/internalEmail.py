import smtplib  
import email.utils
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpUsername = os.environ['SMTP_USERNAME']
smtpPassword = os.environ['SMTP_PASSWORD']
smtpHost = os.environ['SMTP_HOST']
smtpPort = os.environ['SMTP_PORT']
senderEmailID = os.environ['SENDER_EMAIL_ID']
emailRecipient = os.environ['EMAIL_RECIPIENT']

senderName='Israrul Haque'
recipients = emailRecipient.split(',')

class internalemailalert:
    def __init__(self, emailSubject, emailbody):
            self.emailSubject = emailSubject
            self.emailbody = emailbody

    def sendMail(self):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self.emailSubject
            msg['From'] = email.utils.formataddr((senderName, senderEmailID))
            msg['To'] = ", ".join(recipients)
            htmlMIMERecord = MIMEText(self.emailbody, 'html')
            # plainMIMERecord = MIMEText(self.emailbody, 'plain')
            # msg.attach(plainMIMERecord)
            msg.attach(htmlMIMERecord)

            # creates SMTP session
            server = smtplib.SMTP_SSL(smtpHost, smtpPort)
            server.ehlo()
            
            # compiler gives an error for wrong credential. 
            server.login(smtpUsername, smtpPassword) 
            
            server.sendmail(senderEmailID, recipients, msg.as_string())
            server.close()

        except Exception as e:
            print ("Error: ", e)

        return emailRecipient