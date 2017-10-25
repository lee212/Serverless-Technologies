import asyncio
import requests
import json
import concurrent.futures
from datetime import datetime

async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        loop1 = asyncio.get_event_loop()
        #res=[]
        for i in range(0,3200):
            data ={"Id":"google-"+str(i),"name":"mountain view-"+str(i)}
            url="https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/970ac94052782aa2caab8c95f619a43fa7391fb985693bb142a27551f12a3842/function/myaction"
            #res.append(
            loop1.run_in_executor(executor,
                                 requests.post,
                                 url,
                                 data
                                )
            #)

        # for response in await asyncio.gather(*res):
        #     print(response.text)


loop = asyncio.get_event_loop()
date1= datetime.now()
print(date1)
loop.run_until_complete(main())
date2= datetime.now()
print(date2)

print("time diff",date2-date1)




