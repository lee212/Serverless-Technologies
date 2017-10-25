import boto3

endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

cos = boto3.resource('s3', endpoint_url=endpoint)

for bucket in cos.buckets.all():
    print(bucket.name)
    for obj in bucket.objects.all():
        print("  - %s") % obj.key

