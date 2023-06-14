import pandas as pd

data = pd.read_csv('Pandasml/car.csv')
#print(data)
""" df = pd.DataFrame(data)
print(df.head(0))
print("*************************")
print(df.head(10))

print("*************************")

print(df[input("enter col")].head(10)) """
#print(df)
""" data1 = [["java","20000","30days"],["python","22000","32days"]]
df = pd.DataFrame(data1,columns=[ "course"    ,"fee" ,   "day"])
print("*****************")
print(df[["fee","day"]])
"""
data2 = {
    "course":["java","python"],
    "fee":[30000,23000],
    "day":["30days","40days"]
}
df = pd.DataFrame(data2,index=["row1","row2"])
print("*****************")
print(df) 