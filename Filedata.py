#os
#json
#csv

class WriteData:
    def DataWrite(s):
        print("write data ")
        fname = input("enter file name")
        file = open(fname+".csv","w")
        file.write("user data")
        file.close()
class ReadData:
    def DataRead(s):
        print("read data")
        fname = input("enter file name")
        file = open(fname+".csv","r")
        for i in file:
            print(i)
        file.close()
class AppendData:
    def Dataappend(s):
        print("append data")
        
        fname = input("enter file name")
        file = open(fname+".csv","a")
        file.write("user data,")
        file.write("user data\n")
        file.close()

while(True):
    input1  = int(input("enter 1 write\n2 read \n3 append\n4 break"))
    if(input1==1):
        obj = WriteData()
        obj.DataWrite()
    elif( input1==2):
        obj=ReadData()
        obj.DataRead()
    elif (input1==3):
        obj=AppendData()
        obj.Dataappend()
    elif(input1==4):
        break
    else:
        print("*******************")