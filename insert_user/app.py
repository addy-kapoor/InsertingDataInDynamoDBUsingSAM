import os
import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    # Parse incoming request body
    body = json.loads(event['body'])
    
    # Example user data, you can modify this to match your use case
    user_data = {
        'userId': body.get('userId'),  # This should be provided in the request body
        'name': body.get('name'),
        'email': body.get('email')
    }

    try:
        # Insert data into DynamoDB table
        table.put_item(Item=user_data)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User created successfully!', 'user': user_data})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error inserting data', 'error': str(e)})
        }
