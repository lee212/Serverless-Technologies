import argparse
import datetime
import pprint
from datetime import datetime
from google.cloud import storage




def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    for i in range(5):
	    storage_client = storage.Client()
	    bucket = storage_client.get_bucket(bucket_name)
	    blob = bucket.blob(destination_blob_name+str(i))

	    blob.upload_from_filename(source_file_name)

	    print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))



bucket_name="kumar-upload-bucket"
source_file_name="test-file-for-upload.jpg"
destination_blob_name="test-file-for-upload.jpg"
date1= datetime.now()
upload_blob(bucket_name, source_file_name, destination_blob_name)
date2= datetime.now()
print("time diff",date2-date1)
