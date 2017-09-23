import boto3
from datetime import datetime

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

date= str(datetime.now())
print(date)


# Create the DynamoDB table.
table = dynamodb.Table('dynamodbupdate')
with table.batch_writer() as batch:
    for i in range(1,1001):
        batch.delete_item(Key={
            'firstname':"XXXX"+str(i),
            'lastname':"YYYY"+str(i)
        })




# Print out some data about the table.
print(table.item_count)
