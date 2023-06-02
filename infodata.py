class Info:
    def __init__(s,name,age):
        s.name=name
        s.age=age
        
    def showdata(s):
        print("info")
        print(s.name)
        print(s.age)
    
    def display(s):
        print("display")

class Emp(Info):
    def __init__(s,salary,name,age):
        super().__init__(name,age)
        super().display()
        s.salary=salary
    
    def display(s):
        print(" Emp info")
        print(s.salary)
        print("**********")
        print(s.name)

obj = Emp("2000","user","30")
obj.display()
obj.showdata()