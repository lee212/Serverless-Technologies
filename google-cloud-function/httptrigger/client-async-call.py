import asyncio
import requests
import json
import concurrent.futures
from datetime import datetime
import configparser

async def main(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        loop1 = asyncio.get_event_loop()
        #res=[]
        for i in range(0,1400):
            data ={"name":"google-"+str(i)}
            #url="https://us-central1-evocative-tide-183917.cloudfunctions.net/helloHttp"
           # res.append(
            loop1.run_in_executor(executor,
                                 requests.post,
                                 url,
                                 data
                                )
           # )

       # for response in await asyncio.gather(*res):
       #     print(response.text)




config = configparser.ConfigParser()
config.read('client.ini')
url = config['gcp']['url'] #'your client id'

loop = asyncio.get_event_loop()
date1= datetime.now()
print(date1)
loop.run_until_complete(main(url))
date2= datetime.now()
print(date2)

print("time diff",date2-date1)




