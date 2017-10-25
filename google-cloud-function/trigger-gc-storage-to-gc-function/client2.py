from google.cloud import storage
import boto
import configparser
import shutil

def run_quickstart():
    GOOGLE_STORAGE = 'gs'
    LOCAL_FILE = 'file'
    # [START storage_quickstart]
    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = 'kumar-upload-bucket'

    print('Bucket {} created.'.format(bucket.name))
    # [END storage_quickstart]

    filename="C:\\independent-study\\AWS-Lambda\\09-20\\serverless\\compare-Serverless-Technologies\\google-cloud-function\\trigger-gc-storage-to-gc-function\\test-file-for-s3.jpg"
    dst_uri = boto.storage_uri(kumar-upload-bucket + '/' + filename, GOOGLE_STORAGE)
    # The key-related functions are a consequence of boto's
    # interoperability with Amazon S3 (which employs the
    # concept of a key mapping to localfile).
    dst_uri.new_key().set_contents_from_file(filename)
    print('Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name))

if __name__ == '__main__':
    run_quickstart()



shutil.rmtree(temp_dir)
