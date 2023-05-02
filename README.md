# API-Gateway-Deployment-Script-in-Python-Boto3
This script deploys an API Gateway with a root resource and a GET method that integrates with a Lambda function using AWS Lambda and Python's boto3 library.

PREREQUISITES

Before you can use this script, you must have the following:

An AWS account with appropriate permissions to create an API Gateway and Lambda function
Python 3 installed on your local machine
Boto3 installed on your local machine (you can install boto3 using pip: pip install boto3)
Configuration

Before you can run this script, you must configure the following variables:

api_name: The name of your API Gateway
region_name: The AWS region where you want to deploy your API Gateway
lambda_function_name: The name of your Lambda function that you want to integrate with your API Gateway
http_method: The HTTP method you want to use (e.g. GET, POST, PUT, DELETE)
Usage

To use this script, follow these steps:

Clone this repository to your local machine: git clone https://github.com/your-username/api-gateway-deployment-script.git
Navigate to the cloned directory: cd api-gateway-deployment-script
Open the deploy_api_gateway.py file in your favorite text editor.
Configure the variables listed under "Configuration".
Save your changes and close the file.
In your terminal, run the script: python3 deploy_api_gateway.py
Contributions

Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue in the GitHub repository.

