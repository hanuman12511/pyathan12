import csv
with open("fcsv1.csv","w") as write1:
    csvw=csv.writer(write1)
    csvw.writerow({"user","30","300"})

with open("fcsv1.csv","a") as write1:
    csvw=csv.writer(write1)
    csvw.writerow({"user1","301","3001"})
with open("fcsv1.csv","r") as read1:
    csvw=csv.reader(read1)
    for i in csvw:
        print(i)