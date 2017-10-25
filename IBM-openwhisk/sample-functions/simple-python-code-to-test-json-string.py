import sys
import json



def test(d):
    print("Hello world", d["name"])
    jsonString='{"key":"'+d["name"]+'"}'
    print(type(jsonString))
    json.loads(jsonString)



if __name__=="__main__":
    d={"name": "satyam"}
    print(type(d))
    a=test(d)
    print(a)
    print(type(a))
