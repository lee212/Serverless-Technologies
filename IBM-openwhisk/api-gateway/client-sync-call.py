import requests
import json
from datetime import datetime

def call():
    for i in range(200):
        data = {"Id":"google-"+str(i),"name":"mountain view-"}
        url="<give the URL of action>"
        res= requests.post(url=url,data=data) #res= requests.post(url=url,data=data)
        #print(res.text)


if __name__=="__main__":
    date1= datetime.now()
    call();
    date2= datetime.now()
    print("time diff",date2-date1)






