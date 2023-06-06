import os
print(os.getcwd())
#print(os.chdir('..'))
#print(os.getcwd())
print(os.listdir())
listdir1 = os.listdir()

for i in listdir1:
    print(i)
    
rname = input("enter rename")
os.rename("rnuser","rnuser2")
listdir1 = os.listdir()

for i in listdir1:
    print(i)

fname = input("create dir")
#os.remove(fname)
os.mkdir(fname)

listdir1 = os.listdir()

for i in listdir1:
    print(i)
fname = input("enter file name for remove")
#os.remove(fname)
os.rmdir(fname)
listdir1 = os.listdir()
for i in listdir1:
    print(i)

fname = input("enter file name")

if fname in listdir1:
    print("file")
    file = open(fname,"r")
    for i in file:
        print(i)
    file.close()
else:
    print("not")