## Troubleshooting

#### readJson is pipeline is not working
```
Install pluging -> Pipeline Utility Steps
```

#### Failed to load plugins
```
java.io.IOException: Failed to load: Authentication Tokens API Plugin (1.4)
java.io.IOException: Failed to load: Checks API plugin (1.5.0)
java.io.IOException: Failed to load: JUnit Plugin (1.48)
java.io.IOException: Failed to load: Matrix Project Plugin (1.18)
java.io.IOException: Failed to load: Jenkins Jira plugin (3.2)
java.io.IOException: Failed to load: JIRA Integration for Blue Ocean (1.24.4)
java.io.IOException: Failed to load: Plain Credentials Plugin (1.7)
java.io.IOException: Failed to load: SSH Credentials Plugin (1.18.1)

# we are using jenkins as code, where after jenkins installation using code we had installed and upgraded few plugins.
# During reboot, jenkins was try to read the config file but it was not able to load the upgraded plugins. 
# Hence, we deleted files and subfolders of plugins under jenkins_home directory.
# Now, it started perfectly.
# Refer Jenkins configuration as code: https://opensource.com/article/20/4/jcasc-jenkins
```
