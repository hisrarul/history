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

#### Update timezone in Jenkins build
[Referred: Jenkins doc](https://www.jenkins.io/doc/book/managing/change-system-timezone/) 
```bash
# Run below in Jenkins script console:
System.setProperty('org.apache.commons.jelly.tags.fmt.timeZone', 'America/New_York')
```

#### Slack notification in Jenkins pipeline
Add below snippet in Jenkins pipeline
```groovy
    post {
        always {
            slackSend channel: 'jenkins', color: COLOR_MAP[currentBuild.currentResult], message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} by ${BUILD_USER}\\n More info at: ${env.BUILD_URL}"
        }
    }
```

#### Copy ssh key into the docker container in Jenkins pipeline
```groovy            
            script {
                    dir('projDir') {
                        withCredentials([file(credentialsId: '00000-0000-000-000-000000', variable: 'myprivatekey')]) {
                        writeFile file: 'private.pem', text: readFile(myprivatekey)
                        sh """
                            docker build -t ${params.ecrRepo}/${params.env}/${params.service}:${commitId} .
                        """
                        }
                    }
                }


# Inside dockerfile either use COPY or ADD
FROM python:3.9
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

ADD private.pem /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
```

