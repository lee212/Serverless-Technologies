import boto3
from datetime import datetime
# Get the service resource.
dynamodb = boto3.resource('dynamodb')

date= str(datetime.now())
print(date)

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='dynamodbupdate',
    KeySchema=[
        {
            'AttributeName': 'firstname',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'lastname',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'firstname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'lastname',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='dynamodbupdate')

# Print out some data about the table.
print(table.item_count)
