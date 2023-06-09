import csv
print(csv)
with open("projectcsv/car.csv","r") as read1:
    csvw=csv.reader(read1)
    col=0
    print()
    com_name={"name","user"}
    car_dict={}
    next(csvw)
    row = 0
    for i in csvw:
        row=row+1
        #print(i[0])
        com_name.add(i[0])
    
    #print(com_name)
    car_com=list(com_name)
    #print(car_com)
   
    for j in range(len(car_com)):
            car=[]
            print(car_com[j])
            print(csvw)
            for k in csvw:
                print("*************************")
                print(car_com[j],end="")
                print(k[0])
                if(car_com[j]==k[0]):
                    car.append(k[1])
            car_dict.update({car_com[j]:car})
      
        
    print(car_dict)
    
    
    