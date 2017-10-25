import boto3
from datetime import datetime
import  concurrent.futures
import asyncio
# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# Create the DynamoDB table.
table = dynamodb.Table('LambdaTable')
print(table.creation_date_time);
async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        with table.batch_writer() as batch:
            loop1 = asyncio.get_event_loop()
            for i in range(1,3200):
                item={
                         'Id': 'google-'+str(i)
                    }

                loop1.run_in_executor(executor,batch.delete_item,item)


loop = asyncio.get_event_loop()
date= str(datetime.now())
print(date)
loop.run_until_complete(main())
date= str(datetime.now())
print(date)
