import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

date= str(datetime.now())
print(date)


# Create the DynamoDB table.
table = dynamodb.Table('dynamodbupdate')
print(table.creation_date_time);

response=table.query(KeyConditionExpression=Key('firstname').eq("XXXX"))

items=response['Items']
print(items)
