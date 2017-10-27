#!/usr/bin/env python 


import boto 


GOOGLE_STORAGE = 'gs' 


uri = boto.storage_uri("", GOOGLE_STORAGE, 2)
conn = uri.connect("966282726893-th8tovqodhtlln1phjtf89mhg9k1eeql.apps.googleusercontent.com", "7C3aKeDIkCe40kt7ddYn6HTt")
x = conn.get_all_buckets()
print x
