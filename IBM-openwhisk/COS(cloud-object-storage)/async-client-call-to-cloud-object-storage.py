import boto3
import asyncio
import concurrent.futures
from datetime import datetime

# Create an S3 client
endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'
s3 = boto3.client('s3',endpoint_url=endpoint)

async def main():
    bucket_name = 'kumarbucket'
    abspath="/home/cc/satyam.jpg"
    loop1=asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for i in range(2):
            filename = 'satyam'+str(i)+'.jpg'
            #abspath=path+"satyam0.jpg"
            #s3.upload_file(abspath,bucket_name, filename)
            loop1.run_in_executor(executor, s3.upload_file,abspath,bucket_name, filename)


print(str(datetime.now()))
loop=asyncio.get_event_loop().run_until_complete(main())
print(str(datetime.now()))

