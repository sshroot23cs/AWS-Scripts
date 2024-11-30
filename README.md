# AWS-Scripts
Shell or Python scripts to automate Day to Day activities with AWS. 

# Activating a Virtual Environment on Windows

This guide provides instructions on how to activate a Python virtual environment on a Windows system.

## Step 1: Create a Virtual Environment

If you haven't already created a virtual environment, follow these steps:

1. **Navigate to your project directory**:
   Open **Command Prompt** or **PowerShell**, and change to the directory where you want to create the virtual environment:

   ```bash
   cd path\to\your\project
   ```
2. Create Virtual env
    ```bash
       python -m venv venv
    ```
3. Activate Virtual env
    ```bash
       venv\Scripts\activate
    ```
4. Using git bash
    ```bash
   source venv/Scripts/activate
    ```
5. To deactivate 
    ```bash
    deactivate
    ```
6. Install requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
7. Set environment variables for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:

   In Command Prompt or PowerShell, run:
   ```bash
   set AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
   set AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
   set AWS_DEFAULT_REGION=us-west-2
   ```
8. if you are using git bash
   ```bash
   export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
   export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
   export AWS_DEFAULT_REGION=us-west-2
   
   ```
9. Use AWS Configuration File Directly (Advanced)
You can directly specify your credentials in the ~/.aws/credentials (Linux/macOS) or C:\Users\YOUR_USER\.aws\credentials (Windows) file. This is where the AWS CLI stores your credentials, and Boto3 will automatically check this file for credentials.

   Example credentials file:
   ``` java
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   ```
Note: To get the access key and password, create IAM user with required permissions. Then for that user generate access key and secrets