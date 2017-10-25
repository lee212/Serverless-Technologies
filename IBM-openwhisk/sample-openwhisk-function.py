#!/usr/bin/env python
import swiftclient
from keystoneclient import client
import os
import re
#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    Global variables                                                               #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#


container_name = 'main_ContainerTest_write'
# File name for testing
file_name = 'example_file.txt'
#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    Establish Keys                                                                 #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#
auth_url=
project=
projectId=
region=
userId=
username=
password=

#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    Establish Connection to IBM Object Storage
#                    And print account details                                                      #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#

IBM_Objectstorage_Connection = swiftclient.Connection(key=password,authurl=auth_url,auth_version='3',
os_options={"project_id": projectId,"user_id": userId,"region_name": region})
x =  IBM_Objectstorage_Connection.get_account()[1]
print x


#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    create a new container                                                         #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#


IBM_Objectstorage_Connection.put_container(container_name)
print "nContainer %s created successfully." % container_name


#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    List all your containers                                                       #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#

# List your containers
print ("nContainer List:")
for container in  IBM_Objectstorage_Connection.get_account()[1]:
	print container['name']

file_name = 'testfile2.txt'

#
#---------------------------------------------------------------------------------------------------#
#                                                                                                   #
#                    traverse the entire hard drive                                                 #
#                    looking for all files that end with .txt                                       #
#                    get the path to the file to be able to read it
#                    connect to IBM object store and write the file from reading the source         #
#                                                                                                   #
#                                                                                                   #
#                                                                                                   #
#---------------------------------------------------------------------------------------------------#


alist_filter = ['txt','TXT','text']
rootDir = '/Users/savio/documents'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
    	if fname[-3:] in alist_filter:
        	picture_location = (dirName+ "/" + fname)
        	print picture_location
        	with open(picture_location, 'r') as example_file:
 					IBM_Objectstorage_Connection.put_object(container_name,fname,contents=example_file.read(),content_type='text')
 					example_file.close()

#---------------------------------------------------------------------------------------------------#                                                                                                    #
#                Take a copy of a file from IBM object store and work with locally                  #
#---------------------------------------------------------------------------------------------------#
Object_Store_file_details =  IBM_Objectstorage_Connection.get_object(container_name, 'myfile.txt')
with open('downloaded_my_file.txt', 'w') as my_copy:
        my_copy.write(Object_Store_file_details[1])
