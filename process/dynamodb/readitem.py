import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)