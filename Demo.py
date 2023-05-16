'''
n=input("enter n")
n1=input("enter n1")
r =int(n)+int(n1)
print(r)
'''
#+ - * / % //
"""n=input("enter n")
n1=input("enter n1")
r =int(n)%int(n1)
print(r)
"""
"""
n=12326
s = n%10
s=6
n=n//10
r= 62321
"""

#+= -= /= *= %= //=
"""n=2
n=n+1
print(n)

"""
#> < >= <= != ==
#and  or not
# true false

"""
n1=7
n1=n1+1
print(n1>0)
"""

#r =(true)?"+":"-";
"""
if(True):
    print()
    print("true")
"""
"""
if False:
    print("true")
else:
    print("false")
"""

"""
if False:
    print("true")
elif False:
    print("true")
else:
    print("false")

if True:
    print("true")
if True:
    print("true")
"""
"""i=1
while(i<=10):
    print(i)
    i=i+1
"""
"""
for i in range(10): # i=0, 1, <
    print(i)
for i in range(2,10): # i=2, 1, <
    print(i)
for i in range(2,10,2): # i=2, 2, <
    print(i)
"""

#data =[3,4]
""" user  = ["user1","user2"]
password=[111,123]
username = input("enter name")
if username in user:
     print("user login")

p=''
r=False
for i in range(len(user)):
    if(username == user[i]):
        r=True
        p=i
        break
print(p)
if(r):
    password1 =int( input("Enter password"))
    if password1==password[p]:
        print("login")
else:
    print("not login")

"""
""" data =[3,4,5,4,6]
data.insert(2,1)

print(data)
data.append(4)
print(data)
data.remove(3)
print(data)
 """

#data ={key:value}
data={"id":1,"name":"user"}
print(data)
print(data['id'])
data={"id":[1,2,3],"name":["user1","user2","user3"]}
print(data)
for i in data.values():
    print(i)
data['age'] = [23,34,54]
print(data)
data.update({"salary":[3,4,5]})

print(data)
#1.login
""" print(sum(data))
print(max(data))
print(min(data))
print(len(data)) """

""" 1.sum
2. max
3 min
4 len
 """
""" print(data)
print(user)
for i in data:
    print(i) """



