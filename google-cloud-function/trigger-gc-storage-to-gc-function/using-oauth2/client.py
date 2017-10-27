import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time
from ConfigParser import SafeConfigParser

# URI scheme for Cloud Storage.
GOOGLE_STORAGE = 'gs'
# URI scheme for accessing local files.
LOCAL_FILE = 'file'

# Fallback logic. In https://console.cloud.google.com/
# under Credentials, create a new client ID for an installed application.
# Required only if you have not configured client ID/secret in
# the .boto file or as environment variables.
'''
config = SafeConfigParser()
config.read('client.ini')
CLIENT_ID = config.get('gcp','client_id') #'your client id'
CLIENT_SECRET =config.get('gcp','client_secretkey')  # 'your client secret'
print(CLIENT_ID)
print(CLIENT_SECRET)
gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)

'''

#  creating a bucket

now = time.time()
CATS_BUCKET = 'cats-%d' % now
DOGS_BUCKET = 'dogs-%d' % now

# Your project ID can be found at https://console.cloud.google.com/
# If there is no domain for your project, then project_id = 'YOUR_PROJECT'
project_id = 'YOUR_DOMAIN:YOUR_PROJECT'

for name in (CATS_BUCKET, DOGS_BUCKET):
  # Instantiate a BucketStorageUri object.
  uri = boto.storage_uri(name, GOOGLE_STORAGE)
  # Try to create the bucket.
  try:
    # If the default project is defined,
    # you do not need the headers.
    # Just call: uri.create_bucket()
    header_values = {"x-goog-project-id": project_id}
    uri.create_bucket(headers=header_values)

    print 'Successfully created bucket "%s"' % name
  except boto.exception.StorageCreateError, e:
    print 'Failed to create bucket:', e


'''
 #   listing the objects in bucket

header_values = {"x-goog-project-id": 'evocative-tide-183917' }

uri = boto.storage_uri('', GOOGLE_STORAGE,debug=2)
# If the default project is defined, call get_all_buckets() without arguments.
for bucket in uri.get_all_buckets(headers=header_values):
  print (bucket.name)


'''

'''
# Make some temporary files.
temp_dir = tempfile.mkdtemp(prefix='googlestorage')
tempfiles = {
    'labrador.txt': 'Who wants to play fetch? Me!',
    'collie.txt': 'Timmy fell down the well!'}
for filename, contents in tempfiles.iteritems():
  with open(os.path.join(temp_dir, filename), 'w') as fh:
    fh.write(contents)
'''
# Upload these files to DOGS_BUCKET.


filename="test-file-for-upload.jpg"
tempdir="."
with open(os.path.join(tempdir, filename), 'r') as localfile:
	dst_uri = boto.storage_uri("kumar-upload-bucket" + '/' + filename, GOOGLE_STORAGE)
	    # The key-related functions are a consequence of boto's
	    # interoperability with Amazon S3 (which employs the
	    # concept of a key mapping to localfile).
	dst_uri.new_key().set_contents_from_file(localfile)
print ('Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name))

shutil.rmtree(temp_dir)  # Don't forget to clean up!
