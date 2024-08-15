



# AWS_KMS
  
Module to work with kms, creates and controls keys to encrypt your data  

*Read this in other languages: [English](Manual_AWS_KMS.md), [Português](Manual_AWS_KMS.pr.md), [Español](Manual_AWS_KMS.es.md)*
  
![banner](imgs/AWS_KMS.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  



## How to use this module

1. Create an AWS account (skip this step if you already have an account). Visit https://aws.amazon.com/ Click "Create an AWS Account." Follow the instructions to sign up, providing the requested information

2. Sign in to the AWS Management Console: https://aws.amazon.com/en/console/ and navigate to the **IAM** console.

3. Click on **Users** and then on **Create User**

4. Under **User Details** provide a username and click Next.

5. Under **Set Permissions** choose the option **Attach Policies Directly** and below attach the policies **AdministratorAccess** and **AWSKeyManagementServicePowerUser**. Click Next and then on **Create User**

6. Go to the profile (top right corner) and click on Security Credentials.

7. Find the **Access keys** section and press **Create access key**.

8. A **Alternatives to root user access keys** checkbox will open, check it and press **Create access keys**.

**Important**: Write down the Access Key ID and Secret Access Key in a safe place. You will need both to configure the module.



## Description of the commands

### Connection to Aws
  
Enter the data for the connection
|Parameters|Description|example|
| --- | --- | --- |
|Access Key Id|The ID of access obtained when creating the credentials||
|Secret Access Key|Value of the secret obtained when creating the credentials||
|Region|Name of the AWS Region.|us-west-2|
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Generate Key ID
  
Use to encrypt and decrypt data
|Parameters|Description|example|
| --- | --- | --- |
|Description|Optional. Key description.|Variable|
|Assign result to a Variable|Variable where the result will be stored|Variable|

### Encript
  
Encrypt plain text
|Parameters|Description|example|
| --- | --- | --- |
|Key ID|Key ID||
|Text to encrypt|Plain text to encrypt||
|Assign result to a Variable|Variable where the encrypted text will be stored|Variable|

### Decrypt
  

|Parameters|Description|example|
| --- | --- | --- |
|Text to decrypt|It uses the result of the Encrypt command, which is the text that was encrypted.||
|Assign result to a Variable|Variable where the decrypted text will be stored|Variable|

### List Keys
  
List all KMS keys available in your account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a Variable|Variable where the key id and description will be stored in case of having it.|Variable|
