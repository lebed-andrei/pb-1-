import json

with open("11.json", "r") as jf:
    x = json.load(jf)
    r = x["json"]
print(r)