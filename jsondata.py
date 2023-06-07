import json
import requests

print(requests)
r= requests.get('https://jsonplaceholder.typicode.com/todos')
#print(type(r))
#print(r)
l =[]
for i in r.json():
    
    print(i['id'])
    l.append(i['id'])
print(l)
if 100 in l:
    print("found")
    
#print(r.json())
#todos = json.loads(r.text)
#print(todos)
#json.dump(type(r))


data ='{"user":"user1","password":"123"}'
""" with open("data.json","r") as read:
    
    print(json.load(read)['user'])
 """    
""" print(json.dumps(read))
    print(json.dump(read)) """
#jsonget = json.loads(data)
#print(json.load(data).read())