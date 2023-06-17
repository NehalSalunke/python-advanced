import json
infile=open(r'./../Data/sample.json')
#print(infile.read())
data=json.load(infile) #converting json data into dictionery and storing it intoz "data" variable.
print(data)
print(data['101']['name'])