## Vault Token Generator Automation

### Overview
This project automates the process of generating Vault tokens using HashiCorp Vault's AppRole authentication. The system performs the following tasks:

* Retrieves Vault role_id and secret_id as environment variables.
* Sends a POST request to the Vault authentication endpoint to retrieve a token using the role_id and secret_id.
* Schedules the task to run periodically using Windows Task Scheduler to automate the process.

### Key Features
1. Vault Authentication: Uses the AppRole mechanism to authenticate and retrieve a Vault token.
2. Environment Variables: role_id and secret_id are stored as environment variables to securely authenticate the process.
3. Automated Scheduling: The task is scheduled to run periodically using Windows Task Scheduler for continuous token generation.

### Prerequisites
1. Java 8 or above.
2. Vault server setup with AppRole authentication enabled.
3. Windows Server for running the Java program and scheduling the task.
4. Set up environment variables for ROLE_ID and SECRET_ID in system environment variables.


### Steps Followed
**1. Java Program:**

* Developed a Java program (VaultTokenGenerator.java) that makes a POST request to Vault's authentication endpoint (/v1/auth/approle/login), passing the role_id and secret_id as JSON payload in the request body.
* The program retrieves the Vault token in the response and prints it.


**2. Environment Variables:**

* We used the setx command to create system-wide environment variables for role_id and secret_id.
* This was achieved using a Java method to programmatically set these environment variables using ProcessBuilder.


**3. Windows Task Scheduler:**

* Configured Windows Task Scheduler to automatically run the Java program at a scheduled time.
* The task was set to execute the Java program from a specific directory (F:/Apps/JRE), with appropriate arguments to specify the classpath and the class to execute.
* This allows the Vault token generation to run automatically at specified intervals without manual intervention.


### Achievable Goals
* Automated Token Generation: By automating the Vault token generation process, the need for manual intervention is reduced, allowing for better efficiency and reliability.
* Scheduled Execution: The task can be scheduled to run periodically using Windows Task Scheduler, ensuring that a valid token is always available when needed.
* Secure Environment Management: Storing sensitive credentials (role_id and secret_id) as environment variables keeps them secure and allows for easier management.

### Usage Instructions

**1. Clone the Repository:**
* Clone or download this repository to your local system.

**2. Set Up Environment Variables:**
* Set your ROLE_ID and SECRET_ID as system environment variables using the setx command or manually in the Environment Variables section of System Properties.

**3. Modify the Java Program:**
* Make sure to replace the Vault URL and any other necessary configurations in the VaultTokenGenerator.java program.

**4. Compile the Java Program:**
* Navigate to the directory containing the Java file and compile it:
```bash
javac VaultTokenGenerator.java
```

**5. Run the Java Program:**

* Execute the program using:
```bash
java VaultTokenGenerator
```

**6. Schedule Using Task Scheduler:**

* Use Windows Task Scheduler to schedule the Java program to run at a desired time (daily, weekly, etc.).

Ref: https://developer.hashicorp.com/vault/tutorials/auth-methods/approle
