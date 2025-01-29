import json
import sys 

with open ("xyz.json", "r") as fh:
    json_data=json.load(fh)
    print(json_data)




for ele in json_data:
    for key, values in ele.items():
        print(key)
        print(values)
        print("==========")
    #print(ele)
