import asyncio
import requests
import json
import concurrent.futures
from datetime import datetime

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        loop1 = asyncio.get_event_loop()
        res=[]
        for i in range(0,100):
            data = {"Id":"google-"+str(i),"name":"mountain view-"+str(i)}
            url="<give the URL of action>"
            res.append(
            loop1.run_in_executor(executor,
                                 requests.post,
                                 url,
                                 json.dumps(data)
                                )
            )

        for response in await asyncio.gather(*res):
            print(response)

loop = asyncio.get_event_loop()
date= str(datetime.now())
print(date)
loop.run_until_complete(main())
date= str(datetime.now())
print(date)



