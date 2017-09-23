import boto3
from datetime import datetime

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

date= str(datetime.now())
print(date)


# Create the DynamoDB table.
table = dynamodb.Table('dynamodbupdate')
print(table.creation_date_time);

table.put_item(
   Item={
        'username': 'XXXX',
        'last_name': 'YYYY',
        'date_added': date,
    }
)


# Print out some data about the table.
print(table.item_count)
