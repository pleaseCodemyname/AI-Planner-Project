# updateitem.py

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')
table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)