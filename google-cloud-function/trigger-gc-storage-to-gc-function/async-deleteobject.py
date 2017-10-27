import argparse
import datetime
import pprint
import asyncio
import concurrent.futures

from datetime import datetime
from google.cloud import storage


async def delete_blob(bucket,destination_blob_name):
	loop1=asyncio.get_event_loop()
	with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
	    for i in range(1600):
		    blob_name=destination_blob_name+str(i)+".jpg"
		    loop1.run_in_executor(executor, bucket.blob(blob_name).delete)
		    print('Blob {} deleted.'.format(blob_name))


bucket_name="kumar-upload-bucket"
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
destination_blob_name="test-file-for-upload"
date1= datetime.now()
asyncio.get_event_loop().run_until_complete(delete_blob(bucket,destination_blob_name))
date2= datetime.now()
print("time diff",date2-date1)
