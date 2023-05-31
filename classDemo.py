user ={"userdata": {"username": ["user1","user2","user3"],"password":[123,456,111],},"product":{"productid":[1,2,3],"productname":["product1","product2","product3"],"qty":[10,20,34],"rate":[200,300,500],"dis":[2,3,5]},"addtocart":{ "pro_id":[],"pqty":[]} }   
class Line:
    def Lineshow(s):
        print("**************show user*****************")
class Product:
    def __init__(s):
        obj = Line()
        obj.Lineshow();
        pdata = user['product'];
        for j  in range(len(pdata['productid'])):
            if(j==0):
                for i in pdata.keys():
                    print(i,end="\t")
            print()
            for i in pdata.keys():
                print(pdata[i][j],end="\t")
    def prodcut_test(s,product):
        print("pro test")
        pos =-1
        pdata = user['product'];
        for j  in range(len(pdata['productid'])):
            if(product == pdata["productname"][j]):
                print(pdata["productname"][j])
                pos =j
                return pos
        return pos
    def ProductBuy(s):
         print("payment")
         cart = user['addtocart']
         rate = user['product']['rate']
         pid = user['product']['productid']
         print(cart)
         print(rate)
         print(pid)
    def Addtocart(s):
        print()
        print("**************   add to cart ******************")
        while(True):
            ch =int(input("enter 1 for product buy and 2 for not"))
            if(ch==1):
                pro_name = input("enter product name")
                pos = s.prodcut_test(pro_name)
                if(pos!=-1):
                    print("product found")
                    qty = int(input("enter qty"))
                    cart = user['addtocart']
                    l1 = user['addtocart']['pro_id']
                    l2 = user['addtocart']['pqty']
                    l1.append(pos)
                    l2.append(qty)
                    print(user)
                    
                else:
                    print("product not  found")
            else:
                break
class Login:
    def __init__(s):
        userlist = user['userdata']['username']
        print(userlist)
        name =input("enter user name")
        pos = -1
        find =False
        
        for i in range(len(userlist)):
            #print(i)
            if(name==userlist[i]):
                
                #print(user["username"][i])
                pos=i
                find =True
                break
        if(find):
            #print(pos)
            password1= int(input("Enter password" ))
            passwordlist = user['userdata']['password']
            for p in user['userdata'].keys():
                if(p=="password"):
                    if(password1 == passwordlist[pos]):
                        print("login")
                        objpro=Product()
                        objpro.Addtocart()
                        objpro.ProductBuy()
                    

objlog = Login()
#obj.ShowUser()