# Import the necessary AWS SDK libraries and modules
import boto3
import json

# Define the name of the API Gateway and the region it will be created in
api_name = 'MyAPIGateway'
region_name = 'us-east-1'

# Create a client for the API Gateway service
apigateway_client = boto3.client('apigateway', region_name=region_name)

# Define the API Gateway's REST API and resources
rest_api = apigateway_client.create_rest_api(name=api_name)

# Define the API's root resource
root_resource = apigateway_client.create_resource(
    restApiId=rest_api['id'],
    parentId=rest_api['rootResourceId'],
    pathPart='')

# Define a method for the root resource
apigateway_client.put_method(
    restApiId=rest_api['id'],
    resourceId=root_resource['id'],
    httpMethod='GET',
    authorizationType='NONE')

# Define the integration between the API Gateway and a Lambda function
lambda_client = boto3.client('lambda', region_name=region_name)
lambda_arn = lambda_client.get_function(FunctionName='my_lambda_function')['Configuration']['FunctionArn']

apigateway_client.put_integration(
    restApiId=rest_api['id'],
    resourceId=root_resource['id'],
    httpMethod='GET',
    integrationHttpMethod='POST',
    type='AWS_PROXY',
    uri='arn:aws:apigateway:{0}:lambda:path/2015-03-31/functions/{1}/invocations'.format(region_name, lambda_arn))

# Define the method response of the API Gateway
apigateway_client.put_method_response(
    restApiId=rest_api['id'],
    resourceId=root_resource['id'],
    httpMethod='GET',
    statusCoode='200',
    responseModels={
        'application/json': 'Empty'
    })

# Define the integration response of the API Gateway
apigateway_client.put_integration_response(
    restApiId=rest_api['id'],
    resourceId=root_resource['id'],
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        'application/json': json.dumps({'success': True})
    })

# Deploy the API Gateway to a stage
apigateway_client.create_deployment(
    restApiId=rest_api['id'],
    stageName='prod')

