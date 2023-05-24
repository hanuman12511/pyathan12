""" dict ={key:value} """

data = {"id":100,"name":"user","age":30}
data1={}

def User(data):
    print(data)
    print(data["name"])
    print(data.keys())
    print(data.values())
    for i in data:
        print(data[i])
    





def userCopy(data):
    print()
    for i in data:
        data1[i]=data[i]
    data1["info"]={}
def userCopyPrint(data1):
    print(data1)
def updateFun1(data):
    print()
    data.update({"password":"12345"})
def updateFun(data):
    print()
    
    data["dept"]="it"
    data['name']="admin"
    data['id']=[1,2,3,4]
    data["name"]=["user1","user2","user3","user4"]
    data['info']=["skfsdjkfhs","sfhsjklhs","sgsjkgsd","sgjksgfs"]
#updateFun(data)
""" updateFun1(data)
User(data)
print("******************")
userCopy(data)
userCopyPrint(data1) """

def DataUpdate():
    data = {}
    while(True):
        print("data insert")
        ch = int(input("enter 1 for value and enter 2 for list"))
        if(ch == 1):
            key = input("Enter key" )
            print("value")
            value = input("Enter key value")
            data.update({key:value})
        elif ch==2:
            key = input("Enter key" )
            print("list")
            num= int(input("enter list num"))
            list1 =[]
            for i in range(num):
                val = input("enter list value")
                list1.append(val)
            print(list1)
            data.update({key:list1})
                
        else:
            print("not ")
            break
    print("*****************")
    print(data)
user ={"username":["user1","user2","user3"],"password":[123,456,111],"product":{"productid":[1,2,3],"productname":["product1","product2","product3"],"qty":[10,20,34],"rate":[200,300,500],"dis":[2,3,5]},"addtocart":{ "pro_id":[],"pqty":[]} }   
def prodcut_test(product):
    print("pro test")
    pdata = user['product'];
    for j  in range(len(pdata['productid'])):
        if(product == pdata["productname"][j]):
            print(pdata["productname"][j])
            return True
    return False

def addtocart():
    print("**************   add to cart ******************")
    while(True):
        pro_name = input("enter product name")
        if(prodcut_test(pro_name)):
            print("product found")
            
            
        else:
            print("product not  found")
            
    
def Product():
    #print("product")
    pdata = user['product'];
    #print(pdata);
    for j  in range(len(pdata['productid'])):
        if(j==0):
            for i in pdata.keys():
                print(i,end="\t")
            print()
        for i in pdata.keys():
                print(pdata[i][j],end="\t")
        print()
    addtocart()
    
        
        
   
    
    
def loginUser():
   
    #print(user)
    name =input("enter user name")
    pos = -1
    find =False
    for i in range(len(user["username"])):
        #print(i)
        if(name==user["username"][i]):
            
            #print(user["username"][i])
            pos=i
            find =True
            break
    if(find):
        #print(pos)
        password1= int(input("Enter password" ))
        
        for p in user.keys():
            if(p=="password"):
                print(user[p][pos])
                if(password1 ==user[p][pos]):
                    #print("login")
                    Product()
           
    
   
loginUser()         
#DataUpdate()

