import sys
import json
def main(dict):
     print("Hello world", dict["name"])
     print(type(dict))
     jsonString='{"key":"'+dict["name"]+'"}'
     return json.loads(jsonString);
    