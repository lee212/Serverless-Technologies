import boto3
import asyncio
import concurrent.futures
from datetime import datetime

# Create an S3 client
s3 = boto3.client('s3')


for i in range(3001):
    filename = 'satyam'+str(i)+'.jpg'
    response = s3.delete_object(
        Bucket='sourcesatyamresized',
        Key=filename
    )
#
# async def main():
#     bucket_name = 'sourcesatyam'
#     loop1=asyncio.get_event_loop()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
#         for i in range(101):
#             filename = 'satyam'+str(i)+'.jpg'
#             #client.delete_object(Bucket=bucket_name,Key=filename)
#             #s3.upload_file(abspath,bucket_name, filename)
#             loop1.run_in_executor(executor, s3.delete_object,bucket_name,filename)
#
# print(str(datetime.now()))
# loop=asyncio.get_event_loop().run_until_complete(main())
# print(str(datetime.now()))
