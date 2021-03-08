# send email using Gmail on port 587

import smtplib
import os

senderEmailID = os.environ['SENDER_EMAIL_ID']
emailPassword = os.environ['SENDER_EMAIL_PASSWORD']
emailRecipient = os.environ['EMAIL_RECIPIENT']

class internalemailalert:
    def __init__(self, emailbody):
        self.emailbody = emailbody

    def sendMail(self):

        # creates SMTP session 
        email = smtplib.SMTP('smtp.gmail.com', 587) 
        
        # TLS for security 
        email.starttls() 
        
        # compiler gives an error for wrong credential. 
        email.login(senderEmailID, emailPassword) 
        # message to be sent 
        message = self.emailbody
        
        # sending the mail to multiple recipients
        recipients = emailRecipient.split(',')
        email.sendmail(senderEmailID, recipients, message) 
        
        # terminating the session 
        email.quit()

        return emailRecipient
