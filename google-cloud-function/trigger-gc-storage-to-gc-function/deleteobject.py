import argparse
import datetime
import pprint
from datetime import datetime
from google.cloud import storage



def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    for i in range(200):
	    storage_client = storage.Client()
	    bucket = storage_client.get_bucket(bucket_name)
	    blob = bucket.blob(blob_name+str(i))

	    blob.delete()

	    print('Blob {} deleted.'.format(blob_name))

bucket_name="kumar-upload-bucket"
source_file_name="test-file-for-upload.jpg"
destination_blob_name="test-file-for-upload.jpg"
date1= datetime.now()
delete_blob(bucket_name,destination_blob_name)
date2= datetime.now()
print("time diff",date2-date1)
