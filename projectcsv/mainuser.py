import csv
print(csv)
com_name={"name","user"}
car_dict={}
list1=[]
with open("projectcsv/car.csv","r") as read1:
    csvw=csv.reader(read1)
    next(csvw)
    for i in csvw:
        #print(i)
        list1.append(i)
        com_name.add(i[0])
car_com=list(com_name)
#print(car_com)
print("*******************")
#print(list1)


for j in range(len(car_com)):
            car=[]
            for k in list1:
                car_info = []
                if(car_com[j]==k[0]):
                    car.append(k[1])
                    
                    
            car_dict.update({car_com[j]:car}) 
print(car_dict) 
print(car_com)
name= input("enter car name")
print(name,end="") 
print(car_dict[name]) 

    
    
    