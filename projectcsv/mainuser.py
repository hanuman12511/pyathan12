import csv
print(csv)
com_name={"name","user"}
car_dict={}
with open("projectcsv/car.csv","r") as read1:
    csvw=csv.reader(read1)
    next(csvw)
    for i in csvw:
        print(i)
        com_name.add(i[0])
car_com=list(com_name)
with open("projectcsv/car.csv","r") as read1:
    csvw=csv.reader(read1)

    for j in range(len(car_com)):
            car=[]
            for k in csvw:
                if(car_com[j]==k[0]):
                    car.append(k[1])
            car_dict.update({car_com[j]:car})
      
        
print(car_dict)
    
    
    