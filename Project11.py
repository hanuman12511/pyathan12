
data = {"id":100,"name":"user","age":30}
print(data.get('id'))
data.pop("id")
data.popitem()
print(data)
data.fromkeys("idd")
print(data)

""" 
del(data)
print(data) """
data.clear()
print(data)