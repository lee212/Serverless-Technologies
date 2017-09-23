from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

#found in the service credentials
client=Cloudant("<username>","<password>",url="<http://username-bluemix.cloudant.com>")
client.connect();
databaseName = "names"


print(client.all_dbs());
print(type(client.all_dbs()));


if databaseName in client.all_dbs():
    my_database=client[databaseName]
else:
    my_database=client.create_database(databaseName)


result_collection=Result(my_database.all_docs,include_docs=True)

print ("Retrieved minimal document:\n{0}\n".format(result_collection[1]))

# myDatabase=client.create_database(databaseName);
# if(myDatabase.exists()):
#     print("hurray it exists")
# else:
#     print("Creating new")
