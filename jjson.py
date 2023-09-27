import json

data = '''{
    "name": "Kyrylo"
}'''

info = json.loads(data)
print(type(info))
print(info)