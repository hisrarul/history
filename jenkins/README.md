## Jenkins pipeline

#### Create user in mysql database using Jenkinsfile
```https://github.com/hisrarul/history/blob/master/jenkins/Jenkinsfile-db-access``` [[1]](https://github.com/hisrarul/history/blob/master/jenkins/Jenkinsfile-db-access)

#### Read JSON file or text in Jenkinsfile
```https://github.com/hisrarul/history/blob/master/jenkins/Jenkinsfile-readJSON``` [[1]](https://github.com/hisrarul/history/blob/master/jenkins/Jenkinsfile-readJSON) [[2]](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/)



#### Error: javax.mail.AuthenticationFailedException: 535-5.7.8 Username and Password not accepted.
Error during Email test during configuration --->> Jenkins >> Manage Jenkins >> Configure system >> Email Notification
```
https://stackoverflow.com/questions/35347269/javax-mail-authenticationfailedexception-535-5-7-8-username-and-password-not-ac
This worked for me:

Login to the gmail account you are sending mail from
Go to Manage your Google Account -> Security -> Less secure app access -> Turn on access (not recommended)
or
Access the URL:
https://www.google.com/settings/security/lesssecureapps
Turn "Allow less secure apps: OFF" to "Allow less secure apps: ON"
```
