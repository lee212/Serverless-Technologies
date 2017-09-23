import boto3
from datetime import datetime

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# Create the DynamoDB table.
table = dynamodb.Table('dynamodbupdate')
print(table.creation_date_time);


print(datetime.now());
with table.batch_writer() as batch:
    for i in range(1,1001):
        batch.put_item(
            Item={
                 'firstname': 'XXXX'+str(i),
                 'lastname': 'YYYY'+str(i),
                 'date_added': str(datetime.now()),
            }
        )
print(datetime.now());

#response=table.query(KeyConditionExpression=Key('username').eq("asha23"))

#items=response['Items']

#print(items)
