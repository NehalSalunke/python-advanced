import json,requests
data=requests.get(r'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/AFG.geo.json')
content=json.loads(data.text)
print(content)
print(content.keys())
print(content['features'])
print(content['features'][0])
print(content['features'][0].keys)
print(content['features'][0]['properties']['name'])
print(content['features'][0]['geometry']['type'])