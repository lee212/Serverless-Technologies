import requests
import json
from datetime import datetime

def call():
    for i in range(200):
        data = {"Id":"google-"+str(i),"name":"mountain view-"}
        url="https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/970ac94052782aa2caab8c95f619a43fa7391fb985693bb142a27551f12a3842/function/myaction"
        res= requests.post(url=url,data=data) #res= requests.post(url=url,data=data)
        #print(res.text)


if __name__=="__main__":
    date1= datetime.now()
    call();
    date2= datetime.now()
    print("time diff",date2-date1)






