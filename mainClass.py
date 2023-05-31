#from user.userData import userData
import user .Login as u


obj = u.Login()
if(obj.loginuser("admin1" ,"1234")):
    print("user login")
else:
    print("user not login") 