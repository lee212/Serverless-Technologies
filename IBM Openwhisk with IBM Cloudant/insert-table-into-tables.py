from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from datetime import datetime

client=Cloudant("636d3e65-c603-43de-90b9-d355c4992b06-bluemix","38094ac5cbc8ced89e66d2d85beb5009011735be0edf0f5aaeb9ed428004ecfd",url="http://636d3e65-c603-43de-90b9-d355c4992b06-bluemix.cloudant.com")
client.connect();
databaseName = "names"


print(client.all_dbs());
print(type(client.all_dbs()));

#'_id': 'julia30'+str(i), # Setting _id is optional

if databaseName in client.all_dbs():
    my_database=client[databaseName]
else:
    my_database=client.create_database(databaseName)


for i in range(1,501):
    data = {
   '_id':'id'+str(i),
    'name': 'XXXX'+str(i),
    'lastname': 'YYYY'+str(i),
    'date': str(datetime.now())
    }
    # Create a document using the Database API
    my_document = my_database.create_document(data)
    # if my_document.exists():
    #     print ('SUCCESS!!')

