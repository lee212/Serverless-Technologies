import argparse
import datetime
import pprint
import asyncio
import concurrent.futures

from datetime import datetime
from google.cloud import storage

storage_client = storage.Client()
async def main():
	bucket_name= "kumar-upload-bucket"
	source_file_name= "test-file-for-upload.jpg"
	bucket = storage_client.get_bucket(bucket_name)
	loop1=asyncio.get_event_loop()
	with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
		for i in range(3200):
			#destination_blob_name="test-file-for-upload"+str(i)+".jpg"
			#blob = bucket.blob(destination_blob_name)
			#blob.upload_from_filename(source_file_name)
			#loop1.run_in_executor(executor, blob.upload_from_filename,source_file_name)
			#print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))

			destination_blob_name="test-file-for-upload"+str(i)+".jpg"
			loop1.run_in_executor(executor, bucket.blob(destination_blob_name).upload_from_filename,source_file_name)
			print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))


bucket_name="kumar-upload-bucket"
source_file_name="test-file-for-upload.jpg"
destination_blob_name="test-file-for-upload.jpg"
date1= datetime.now()
loop=asyncio.get_event_loop().run_until_complete(main())
date2= datetime.now()
print("time diff",date2-date1)
