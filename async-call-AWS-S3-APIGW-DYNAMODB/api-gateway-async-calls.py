import asyncio
import requests
import json
import concurrent.futures

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        loop1 = asyncio.get_event_loop()
        res=[]
        for i in range(1,3000):
            data = {"operation":"create","tableName":"LambdaTable","payload":{"Item":{"Id":"google-"+str(i),"name":"mountain view-"+str(i)}}}
            url="https://2pcprzeela.execute-api.us-east-2.amazonaws.com/prod/DynamoDBManager"
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
loop.run_until_complete(main())



