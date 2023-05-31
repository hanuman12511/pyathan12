import data.data as data
class User:
    def userLogin(s):
        name = input("enter user name")
        
        print(data.user)
        if name in data.user:
            return True
        else:
            return False
        
    