Generative Artificial Intelligence (generative AI) is an artificial intelligence capability that creates new content and artifacts such as text, code, images, audio, and video. Unlike traditional AI systems that analyze data, generative AI models can produce novel human-like outputs.

These models are trained on vast datasets to learn patterns and relationships within the data. They can then use what they have learned to generate entirely new examples similar to the training data but not identical. For instance, a generative AI model trained on images of animals could create convincing images of animals it hasn’t seen before.

Potential applications of generative AI include generating conversational agents, translating text, composing music, creating artificial art, generating code comments, automating computer coding, and more.

Generative AI promises to open up new possibilities in several domains, enhancing productivity across many industries and disciplines, including the Software Development Life Cycle (SDLC).

For a more detailed dive into generative AI, see [What is generative AI and Amazon Q](https://aws.amazon.com/what-is/generative-ai/).

## What to expect from this Immersion Day?
In this immersive workshop, you will explore the transformative impact of generative AI on the development activities, allowing you to apply [next-generation developer experience](https://www.youtube.com/watch?v=8mUosAh3gLc)  concepts throughout your SDLC. You will gain practical insights into how generative AI can significantly enhances your efficiency.

Through hands-on sessions, you will:

`Discover and use generative AI tools`: Learn how to integrate AWS's generative AI tools into your development process. These tools will assist you in generating high-quality, context-specific guidance.
`Automate repetitive tasks`: Understand how to utilize generative AI for automating repetitive and well-defined development tasks. This will free up your time, allowing you to focus on high-value, innovative aspects of your day-to-day.
`Use generative AI tools for application modernization`: Engage with AWS generative AI tools from the AWS Console and your IDE.
`Gain hands-on experience with AWS Services`: Get acquainted with Amazon Q Developer. This will include practical exercises in application modernization, enhancement, and leveraging generative AI tools to optimize your development processes.


#### Introduction
Throughout this Immersion Day, you will work on different tasks to maintain, develop, and troubleshoot an electronic wallet application, named E-wallet. You will use generative AI tools, and apply next generation development experience concepts to various phases of the Software Development Lifecycle (SDLC).

Each module is independent, so you can choose which sections you would like to complete!

#### Persona
In this workshop, you take on the role a developer tasked with maintaining and enhancing an existing E-wallet application. Your experience in building microservices is invaluable to the project. Though you may not consider yourself an AWS expert, you are acquainted with essential AWS services such as AWS Lambda, Amazon API Gateway, and Amazon DynamoDB, and have basic programming skills in Python. Your team employs a CI/CD pipeline to streamline the deployment of updates, highlighting the workshop's focus on a developer-oriented approach.

#### E-wallet application
You will be working on the E-wallet application.

Customers can hold a balance in different currencies, top up, withdraw, and transfer money to other E-wallets. Customers can also use their E-wallet as a payment method, integrating with 3rd-party payment providers.

Time to production, cost savings, and applying best practices are common goals for your team. You would like to minimize costs as much as possible while ensuring performance is not impacted. It is expected that the user base will rapidly expand. You would like to ensure that the application can scale to cope with increased number of users with variable access patterns.

The E-wallet use cases are:

As a customer, I want to see my current balance in a given currency.
As a customer, I want to list my current balances in all currencies.
As a customer, I want to top up my E-wallet using different currencies.
As a customer, I want to transfer money to an E-wallet that belongs to another customer.
As a customer, I want to withdraw money from my E-wallet into my bank account using International Bank Account Number (IBAN).
As a customer, I want to use my E-wallet as a payment method for online shopping.


## Generative AI for Builders
#### Benefits of generative AI in the Software Development Life Cycle
The rapid evolution of generative AI presents exciting opportunities to transform the Software Development Life Cycle (SDLC). Developers are beginning to tap into the creative potential of generative AI to automate repetitive coding tasks, generate test cases, fix bugs, optimize code, summarize and explain code, and accelerate many other parts of the SDLC. By integrating generative AI capabilities into their toolchain, engineering teams can boost productivity, reduce costs, and quickly bring innovations to market.

Amazon Q Developer provides an AI assistant to support developers and builders at each stage of the development process - from researching to deploying to upgrading. The integration into existing developer tools helps accelerate the development workflow.

In this module, you’ll get to experience some of these optimizations through the use of Amazon Q capabilities that allow you to:

* `Quickly access answers and ideas through conversational Q&A`, directly within tools like the AWS console and the IDE. This helps save time researching or looking up information.
* `Troubleshoot errors and issues` directly within the console for various AWS services, providing analysis and proposed solutions. This helps resolve problems faster.
* `Identify security vulnerabilities` in code from within the IDE, providing options for auto resolution. This helps improve the security of your applications.
* `Guide you through new feature development` interactively within the IDE with step-by-step instructions. This helps build new features quicker.
* `Upgrade code` by through the generation of transformation plans. This simplifies maintaining and upgrading applications.

For more information on Amazon Q capabilities see [Amazon Q Developer, now generally available, includes new capabilities to reimagine developer experience](https://aws.amazon.com/blogs/aws/amazon-q-developer-now-generally-available-includes-new-capabilities-to-reimagine-developer-experience/).



## Creating Effective Prompts
#### Prompt engineering
Prompt engineering is the process where you guide generative artificial intelligence (generative AI) solutions to generate desired outputs. Even though generative AI attempts to mimic humans, it requires detailed instructions to create high-quality and relevant output. In prompt engineering, you choose the most appropriate formats, phrases, words, and symbols that guide the AI to interact with your users more meaningfully. Prompt engineers use creativity plus trial and error to create a collection of input texts, so an application's generative AI works as expected.

A prompt is a natural language text that requests the generative AI to perform a specific task. Generative AI is an artificial intelligence solution that creates new content like stories, conversations, videos, images, and music. This is powered by very large machine learning (ML) models that use deep neural networks, pre-trained on vast amounts of data.

#### Prompts in the Software Development Life Cycle
During this workshop you will be writing Amazon Q Developer prompts through the IDE the AWS Console. The interaction from the IDE or the Console caters to different aspects of the development process, making the experience of writing prompts unique in each case. These will include:

Prompting for inline completion in the IDE. Developers can insert prompts inline and leverage code auto-complete. Q uses prompts to grasp the intended functionality or feature, generating corresponding code. This method is particularly beneficial for quickly creating standard code, complex algorithms, or creating unit tests.

Prompting in the command line. Extending to the command line, Q allows developers to use its features via terminal commands. This functionality is ideal for those who prefer or need to work within a command-line environment that offers natural language-to-bash translation. The command line tool also assists with auto completion for 500+ CLIs.

Prompting in Q chat. Q's Chat in IDE feature offers a conversational interface for coding assistance, allowing developers to pose questions in a chat-like format. This approach is ideal for clarifying programming concepts, resolving errors, and explaining code. Q is a virtual coding assistant that provides more interactive and engaging guidance and suggestions.

Prompting in the AWS Console. Within the AWS Console, Q operates through a chat interface. This mode is particularly effective for cloud resource management and troubleshooting.

#### Best practices
Let us dive into some best practices for formulating a great prompt!

**Be specific and clear**. It is critical to write prompts in a specific and clear manner to get desired responses. You should state the task directly and provide as much detail as possible.

* Clarity involves the accuracy and specificity of the prompt. A clear prompt leaves little room for misinterpretation, guiding Q to generate the desired response type or action. Lack of clarity may result in irrelevant or off-target responses. Clear prompts are essential in inline completion tools like Q, where precise coding solutions are required.

* Intent refers to the purpose or goal behind the prompt. Understanding the user's intent allows Q to generate accurate and relevant responses to your objectives. For instance, if the intent is to create a block of code to solve a specific problem, the prompt should reflect that goal.

* Context involves the surrounding information or environment related to the prompt. This includes factors like the state of the code in a file, which might be a new file or one that's fully established, shaping how Q approaches inline completion. Similarly, the subject of a conversation or past interactions with Q can also inform its responses. Context allows Q to offer tailored responses that are more in sync with the user's current needs. For instance, Q's response to a code snippet is influenced by the existing code, while in Q's chat interface, the flow of the ongoing conversation is a critical contextual element.

**Use examples**. Enhance your prompts by including relevant examples, as this strategy guides Q to produce better outputs by providing additional context. Consider the different ways a prompt might be handled in a new file versus an established file and how this context can elevate the quality of the suggestions. This distinction is important and can be applied by keeping relevant open files or adding inline with the current file.

**Use an iterative approach**. Don't hesitate to refine and rephrase your prompts based on responses. This iterative approach is critical to achieving your desired results. The ease of this process varies depending on the tool used: for instance, in a Q chat window, iterating is straightforward, as you can easily ask in the chat conversation. However, Q's inline completion requires you to go back and edit the original prompt directly.

**Break down complex queries**. For complex queries, breaking down the prompt into smaller, more manageable parts can be effective. This approach helps in guiding Q step-by-step to the desired output.

**Understand the nondeterministic nature**. Generative AI tools, by their very nature, are nondeterministic. This refers to the responses or suggestions provided by tools like Amazon Q which can vary each time a query is posed, even if the prompt and context remain the same. As a result, the output of these tools is not fixed but dynamic, reflecting the latest state of their training and the current context of the prompt. Additionally, as these models are updated and improved over time, the nature of the responses can change. You should be prepared for this fluidity and understand that the suggestions are guidance rather than definitive answers. This nondeterministic quality is both a strength, offering a range of possibilities and fresh perspectives, and a challenge, necessitating critical evaluation and contextual consideration of each response.

#### Amazon Q
```"Explain how to implement auto-scaling for an EC2 instance group based on CPU utilization."```

* **Why?** This prompt is specific, requesting detailed instructions for a particular task (auto-scaling based on CPU utilization).
* **Prompt to avoid.** "How do I use EC2?". This prompt is overly broad and doesn't specify what aspect of EC2 you need information on.

#### Inline Completion
* ```"Create a JavaScript function to sort an array of numbers in ascending order."```

* **Why?** This prompt is specific about the programming language (JavaScript), the task (sorting an array), and the criteria (ascending order).
* **Prompt to avoid.** "I need help with an array." This prompt lacks specificity. What is the operation needed on the array, or the nature of the help required?


## Aligning Expectations and Best Practices
As we dive deeper into using generative AI, it's essential to align expectations with the actual capabilities of these tools. Generative AI has made significant strides, offering innovative solutions and automating complex tasks. However, it's equally important to recognize its limitations.

#### Capabilities of generative AI
* **Complex problem-solving:** Generative AI excels in solving complex problems, generating solutions, and code translation.
* **Content generation:** It can create code, answer relevant answers to pressing questions, solve problems, and take action using the data and expertise found in your company's information repositories, code, and enterprise systems.
* **Language understanding and interaction:** Generative AI shows a strong understanding of natural language, enabling it to engage in meaningful conversations, answer questions, and provide explanations.
Limitations of generative AI
* **Dependence on training data:** The output quality heavily depends on the training data's quality and breadth. Q is a generative AI service powered by a [Foundation Model  (FM)](https://aws.amazon.com/what-is/foundation-models/) trained on various data sources, including Amazon and open-source code. Amazon Q is built on Amazon Bedrock, a fully managed service for building generative AI applications that offers a choice of high-performing FMs from Amazon and leading AI companies. Amazon Q uses multiple FMs to complete its tasks and uses logic to route tasks to the FM that is most appropriate for the context of the prompt.

Q inline code suggestions supported programming languages: In the context of inline code suggestions, there are limitations in the range of supported programming languages. This means that the service does not automatically support your language of choice. For a current list of supported languages, refer [Language support for inline suggestions  documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-language-ide-support.html#inline-sugestions-language-support).

Accuracy and fact-checking: Generative AI can sometimes produce plausible, but factually incorrect information, necessitating human verification in critical applications.


## Understanding, Optimizing, and Fixing Existing Code
#### Introduction
In this module, you will be tasked with going through various aspects of onboarding for this new E-wallet application. The goal is to understand, optimize, and fix the existing code within the application stack.

#### Background
You have just cloned the initial version of the E-wallet application that another team has been working on. You are new to this project, and am looking to understand how it's organized, the main components, and how the application functions. Although you have searched for documentation, there is little available besides the README.md file.

#### Objectives
We will use Amazon Q chat in the IDE to go through the following tasks:

* Task 1 - Onboarding.
* Task 2 - Code optimization.
* Task 3 - Fixing existing code.

## Task 1 - Onboarding
#### Situation
The first thing you decide to do is learn the application's architecture, which components exist and how they are used.

You see the project uses the AWS Cloud Development Kit (CDK) for infrastructure and application components. You have limited experience using CDK, so you would like to become more familiar on that topic.

Finally you would like to understand how the withdraw feature was implemented. From an initial investigation, you have identified that the withdraw.py file containing business logic to handle withdraw transactions.

#### AWS Cloud Development Kit familiarization
After reviewing the README.md file in the project, you see that CDK is being utilized in this application. You decide to start by becoming more familiar with CDK, before investigating how it is used for the various components in the application.

1. Open the Amazon Q Chat window in your IDE by selecting the `Q Icon` on the left-hand pane as shown below:
2. Enter a prompt in the Amazon Q Chat pane to better get more information on CDK.
    a. What is AWS CDK?
    b. Can you provide details around what the AWS Cloud Development Kit is?
    c. Can you explain what AWS CDK is?

#### Understanding application components
Now that you have a background understanding of CDK, you will get further details about the different CDK components in the E-wallet application.

1. Open the ewallet/ewallet_stack.py file in your IDE. This ensures that Amazon Q has the correct context for your question.
2. Enter a prompt in the Amazon Q Chat pane to gain insight into your different infrastructure components.
    a. Can you explain all the infrastructure components I have declared for my CDK application?
    b. What are the different CDK components in my application that are declared?
    c. In my ewallet_stack.py file, can you list all components in my CDK application?


####  Application code familiarization
Now that you have an understanding of the infrastructure components, you would like to investigate the withdraw functionality. To start, let's analyze a file containing the application code.

1. Open the `ewallet/controller/withdraw.py` file. In the withdraw.py file select all the code and right click. From the pop-up, choose Send to **Amazon Q -> Explain**

Amazon Q explains to you the various aspects of what the application is doing such as validating the request payload, loading the Amazon DynamoDB tables, and more. You would like to know more about what validation is being applied in the code.

2. With the `withdraw.py` file still open, prompt Amazon Q to understand more about the payload validation.

**Hint**
Ask Amazon Q about the kind payload validation the application is doing.

#### Sample prompts
* What kind of payload validation is this application doing?
* Is this class doing payload validation?
* What specific validation is the application doing in my withdraw.py file?


## Optimizing code
You will use Amazon Q help optimize the `validation_payload` method.

1. Keeping the `ewallet/controller/withdraw.py` file open, highlight the validate_payload method. Right-click and from the pop-up menu, choose Send to Amazon Q, Optimize.


#### Adding a dictionary
After deciding to proceed with using the dictionary, you decide to utilize Amazon Q to provide the code to implement this solution.

Prompt Amazon Q to provide a code sample for this solution.
1. Can you provide a code sample to utilize a dictionary to perform the validations?


## Task 3 - Fixing Existing Code
#### Situation
You find that the AWS Lambda function intermittently fails when loading a transaction from the Amazon DynamoDB table. After further investigation, you suspect that there is a bug in the find method in the dynamodb_wallet_repository.py file.

#### Fixing code
Investigate the find method within the DynamoDbWalletRepository class.

1. Open the `ewallet/repository/dynamodb_wallet_repository.py` file. Find and select the find method and right click. From the pop-up, choose Send to Amazon Q,
2. Now in the Q chat pop-up window, enter a prompt to help you fix the potential issue causing failed transaction loading on the DynamoDB table.

## Editing New and Existing Code
#### Introduction
The section focuses on how you can use Q to enhance developer productivity with inline completion.

#### Background
You are facing a tight deadline, with a code review meeting scheduled for the next day. The E-wallet application requires urgent updates and the addition of new features. You would like assistance to expedite the development process, including updating the current code and integrating new functions to finalize the E-wallet application. For this section you will use Amazon Q as a solution to these development challenges.

#### Objectives
This Q module will cover the following items:

* Key commands and basics.
* Prompt engineering.
* Task 1 - Enhancing E-wallet functionality with Q inline completion.
* Task 2 - Shipping new features faster.
* Task 3 - Generating E-wallet unit tests.


## Key Commands and Basics
#### Q key commands
To interact with Q while editing your code, you can use comments to trigger suggestions or have it complete your code as you type. Q can be triggered manually using the shortcut commands, or the auto-suggestions will assist with completing code as you type.

Cycling through up to 5 suggestions using the Forward (→) and Backward (←) keys. To accept a recommendation, hit Tab.

To force a recommendation can be achieved by hitting `Option + C` on macOS or `Alt + C` on Windows.

| Action | Keyboard shortcut|
|--------|------------------|
| Manually trigger code whisperer | Option + C (Mac)
| Accept a recommendation | Tab
| Next recommendation | Right arrow
| Previous recommendation | Left arrow
| Reject a recommendation | Esc, Backspace


Other user actions are viewable at the link provided [here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/actions-and-shortcuts.html).

#### Q inline completion basics
Take a look at the various ways to interact with Q to generate helpful code recommendations:

* Multi-line comments.
* Leveraging auto-complete.
* Context is taken from the comment and existing code.
* Writing unit tests.
* Manually trigger Q to offer a suggestion.

#### Example 1 - Leveraging auto-complete
You can allow Q to make recommendations as you type.

In this example, you create an array of fake E-wallets for testing.

1. Open the file `basics/example1.py`.
2. Place your cursor at the end of the second line and press Enter to add a new line. Q should recommend a new fake E-wallet. Press Tab to accept the entry. Use Q's suggestions to add a few more items. When complete, press Escape to stop the recommendations.

#### Example 2 - Multi-line comments
In this example, you will use a multi-line comment to generate code.

1. Open the file `basics/example2.py`.
2. Navigate to the end of the comment, and hit return. Q will provide code that meets the requirements specified in the comments.

#### Example 3 - Manually triggering Q to offer a suggestion
You can also manually trigger Q to offer a suggestion by pressing either Option + C on macOS or Alt + C on Windows.

1. Open the file `basics/example3.py`.

The file has a single import statement on line 5. Place your cursor on line 6 and trigger Q manually using the key combination above.

You have manually triggered Q, and it will suggest importing another package.



## Prompt Engineering
Now that you have reviewed Q's key commands and ways to interact with them, let us understand how to use prompt engineering to produce tailored code recommendations.

This guide covers the basics of using prompts to interact with Q. Q can be leveraged for various development tasks.

You can follow along using the files in prompt-eng/ in the project you cloned previously.

#### Example 1 - How additional context matters
While specific and concise prompts are crucial, additional context can aid Q comprehension. Concrete examples also guide Q if it struggles to infer expectations from a brief prompt.

You would like to store the CSV file content in a dictionary and return the objects. Take a look at the sample prompt below. Judicious context helps Q to produce higher-quality, tailored results.

1. Open the file prompt-eng/example1.py.
```bash
# function that accepts a path to a csv file and returns the content as a dictionary
```


#### Example 2 - Utilizing multiple comments
Multiple comments can be a helpful technique in prompt engineering. When used strategically, multiple comments allow developers to offer more context without sacrificing brevity or cluttering the prompt.

Your requirements are:

1. Open a CSV file.
2. Alphabetize the CSV lines in a list.
3. Insert a period at the end of each line.

Take a look at the sample Q prompt below. Notice how you can break up multiple requirements into separate comments.

1. Open the file prompt-eng/example2.py, and get Q to generate a code block based on the comments.
```text
# open a csv file and return the list of lines in alphabetical order
# remove duplicate lines
# insert a period at the end of each line
```


#### Example 3 - Context taken from comments and code
Q's context extends beyond comments to encompass the surrounding code, including other functions, imports, and more. This expanded context is instrumental in guiding Q to implement the intended use case derived from the comments.

You will explore how additional code in the project influences responses. The approach involves importing the pandas library to observe its effect on recommendations, contrasting with the previous section.

1. Open the file `prompt-eng/example3.py`.

```text
import pandas as pd
# open a csv file and return a list of lines in alphabetical order
# insert a period at the end of each line
# replace duplicate lines with a single line
```
2. Use Q to generate the required function.

#### Example 4 - Prompt as-you-go
Breaking down a complex coding project into smaller, more manageable segments allows Q to provide highly accurate and tailored suggestions for each comment. Comments are often placed above function or class declarations; however, they can be placed anywhere within the source file, including within the function definition. Segmenting your development tasks with incremental guidance can help Q to understand the developer's intent more clearly.

In this example, you will examine a code snippet generated by Q that contains multiple comments. This code snippet will ask the the user to input a filename, ensure it’s a CSV and alphanumeric, and then process it with the logging.info method.

You will analyze the output using both the prompt as-you-go approach and a single prompt in the file prompt-eng/example4.py.

#### Prompt as-you-go example
Get Q to generate a code block based the comments:

1. # take a user’s input using the input() function and store it in a variable called filename.
```text
import logging
# take a user's input using the input() function and store it in a variable called filename
filename = input("Enter the name of the file you want to read: ")
```

2. # create a function that will take a filename as an input.
```text
import logging
# take a user's input using the input() function and store it in a variable called filename
filename = input("Enter the name of the file you want to read: ")

# create a function that will take a filename as an input
def open_file(filename):
```

3. # validate the input using the isalnum() method and ensure the file ends in .csv then process the file using logging.info().
```python
import logging
# take a user's input using the input() function and store it in a variable called filename
filename = input("Enter the name of the file you want to read: ")

# create a function that will take a filename as an input
def open_file(filename):
  #validate the input using the isalnum() method and ensure the file ends in .csv then process the file using logging.info()
  if filename.isalnum() and filename.endswith('.csv'):
    lines = open_csv(filename)
    logging.info(lines)
    return lines
  else:
    print('Invalid file name')
    return None
```


#### Single prompt example
1. Use Q to generate the required function:
```python
import logging
'''
Using the input() function and store it in a variable called filename and create a function
that will validate the input using the isalnum() method and ensure the file ends in .csv then process
the file accordingly.
'''
def validate_file(filename):
  if filename.isalnum() and filename.endswith('.csv'):
    return True
  else:
    return False

```

When analyzing these side-by-side, you see that with the 'prompt as-you-go approach', using multiple comments to segment larger development tasks allow Q to gain clarity of the developer's intent. Q successfully helped to implement all the requirements.

On the other hand, when a single comment implemented multiple requirements, Q didn't consider all the requirements for this slightly more complex problem. Prompting as-you-go allows large language models like Q to produce more accurate code about the use case by breaking down complicated issues into logical steps. This results in more precise code to the desired functionality than a single broad prompt.

You are now ready to get started with the first task using Q inline completion!


## Task 1 - Enhancing E-Wallet Functionality
For this challenge, you will enhance the user-friendliness of the E-wallet application by adding new functionality.

The challenge involves accomplishing two specific tasks:

Add the capability to get a E-wallet's total number of transactions.
Allow a user to filter out transactions in the E-wallet.
Challenge overview
In the model directory, open the file ewallet/model/wallet.py. The file already contains the existing code with several methods for handling transactions and balances in the E-wallet app.

Existing code
The file already has basic E-wallet functionalities that users can utilize to check their balances, list their balances, list all of their transactions, withdraw money from the wallet, and load and transfer money to and from the wallet.

You will use Amazon Q to streamline the development of the two assigned tasks.

#### Adding capability to get the total number of transactions in a wallet
You will add a new function to the ewallet/model/wallet.py file. This function, placed at the end of the file within the Wallet class, will enable users to retrieve the total number of transactions in their e-wallet. It's designed to simplify the user experience, providing a straightforward method for monitoring the overall transaction count in the e-wallet app.

Open the ewallet/model/wallet.py file.

Use Q to suggest a code block for the new function.

Sample prompt
  # function to get total number of transactions of the wallet

Solution
Great news! You have completed the first task!



Transaction history filtering
The second enhancement is to incorporate another function to the Wallet class. This will allow users to filter out their transactions based on a transaction type, providing a user-friendly way to keep track of their financial activities.

Use Q to suggest a code block for the new function.
Sample prompt
130
  # function to filter out transaction list based on transaction type




## Task 2 - Shipping New Features Faster
In the previous task, you investigated how Amazon Q can help expedite working with existing code and becoming familiar with the code base. In this section, you will continue to use Amazon Q to help author new functionality.

Background
You are looking to rapidly implement user and invoice-related enhancements to the E-wallet application.

The following feature request covers the desired functionality.

Title: List existing E-wallets
Description: This feature will allow users to list the E-wallets they created for various purposes.
List existing E-wallets
In the directory ewallet/controller, open and browse the file create_wallet.py. This is where the create wallet controller function is implemented. You will write a similar controller for listing E-wallets.

Open the file list_wallet.py in the same directory. You will notice it only a few import statements.

You will use Q to help us implement the list wallets function after the import statements. Q will use contents from both controller files as context.

3. Use Q to suggest code to create a new logger.
Sample prompt
10
# create a logger at the INFO level

4. Create an accessor for the wallet repository class. This should be similar to the wallet creation implementation.
Sample prompt
14
# function to get wallet repository using dynamodb client and table name

5. Implement the list wallets function.
Sample prompt
19
# function to list wallets using the wallet table name, including comments to explain each line

Solution
In the above code snippet, Q suggests calling the list_wallets() function in the wallet repository class. By browsing the DynamoDbWalletRepository function in the file ewallet/repository/dynamodb_wallet_repository.py, you will notice that it performs a scan operation of the database table to return all items.

Finally, write the Lambda handler function for this controller to call the function created.
Sample prompt
28
# create the lambda handler function



## Task 3 - Generating E-Wallet Unit Tests
In this module you will use Q to facilitate the rapid generation of unit tests.

Challenge overview
In the directory tests/unit/model, open the file test_wallet.py. This file contains a WalletTest class, which needs more test case functionality added.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```python
import unittest
import sys
sys.path.append('.')

import boto3
from ewallet.model.wallet import Wallet
from ewallet.model.transaction import TransactionType, TransactionStatus

class WalletTest(unittest.TestCase):

  def test_wallet_creation(self):
    wallet = Wallet('test_wallet')
    self.assertDictEqual(wallet.balance, {})
    self.assertCountEqual(wallet.transactions, [])
    self.assertEqual(wallet.id, None)
    self.assertEqual(wallet.name, 'test_wallet')

  def test_list_balance(self):
    wallet = Wallet('test_wallet')
    wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
    wallet.add_transaction(300, 'EUR', TransactionType.TOP_UP)
    wallet.add_transaction(50, 'GBP', TransactionType.TOP_UP)
    wallet.withdraw(50, 'GBP')

    balance = wallet.list_balance()

    self.assertListEqual(balance, ['USD 100.00', 'EUR 300.00', 'GBP 0.00'])
```
As illustrated, this test mocks the wallet_creation and list_balance function in the Wallet class. You will add a test case in this section. After updating the code, open a new terminal and run the following command below in the demo-serverless-microservice root directory to check if the test cases pass successfully:

pytest -W ignore tests/unit/model/test_wallet.py

#### Test E-wallet top up functionality using Q
Firstly generate a test that tests the top up functionality to top-up funds in the E-wallet.

Use Q to generate the unit test function.
Sample prompt
29
  # create a function that tests top_up


#### Test E-wallet transfer functionality using Q Chat
Now tht you have seen how to use Q to generate unit test code, let's look at how Amazon Q can similarly generate unit tests. You will implement a test whether the transfer method accurately transfers funds from one E-wallet to another.

1. Open the Amazon Q Chat and ask the chatbot: Create a function that tests transfer from one wallet to another wallet and checks for the accurate balance.

Full Solution for test wallet
```python
import unittest
import sys
sys.path.append('.')

import boto3
from ewallet.model.wallet import Wallet
from ewallet.model.transaction import TransactionType, TransactionStatus

class WalletTest(unittest.TestCase):

  def test_wallet_creation(self):
    wallet = Wallet('test_wallet')
    self.assertDictEqual(wallet.balance, {})
    self.assertCountEqual(wallet.transactions, [])
    self.assertEqual(wallet.id, None)
    self.assertEqual(wallet.name, 'test_wallet')

  def test_list_balance(self):
    wallet = Wallet('test_wallet')
    wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
    wallet.add_transaction(300, 'EUR', TransactionType.TOP_UP)
    wallet.add_transaction(50, 'GBP', TransactionType.TOP_UP)
    wallet.withdraw(50, 'GBP')

    balance = wallet.list_balance()

    self.assertListEqual(balance, ['USD 100.00', 'EUR 300.00', 'GBP 0.00'])

  # create a function that tests top_up
  def test_top_up(self):
    wallet = Wallet('test_wallet')
    wallet.top_up(100, 'USD')
    self.assertEqual(wallet.balance['USD'], 100)
    self.assertEqual(len(wallet.transactions), 1)
    self.assertEqual(wallet.transactions[0].amount, 100)
    self.assertEqual(wallet.transactions[0].currency, 'USD')
    self.assertEqual(wallet.transactions[0].type, TransactionType.TOP_UP)

  def test_transfer_balances(self):
    # arrange
    wallet1 = Wallet('wallet1')
    wallet2 = Wallet('wallet2')

    wallet1.top_up(100, 'USD')

    # act
    wallet1.transfer(50, 'USD', wallet2)

    # assert balances
    self.assertEqual(wallet1.balance['USD'], 50)
    self.assertEqual(wallet2.balance['USD'], 50)
```

```bash
pytest -W ignore tests/unit/model/test_wallet.py
```
