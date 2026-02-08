import pandas as pd


df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


df.sort_values("Age")
#print(df.sort_values("Age"))


df.sort_values("Age",ascending=False,na_position="first")
df.sort_values("Age",ascending=True,inplace=True) # na_position = "last" oluyor otomatik
#print(df)

print(df.sort_values(["Age","Salary"],ascending=[True,False]))   # önce age sonra salary

df = df.sort_index()
print(df)

df2 = df.nlargest(10,"Salary")
print(df2)

df3 = df.nsmallest(10,"Salary")
print(df3)

print(df2.reset_index())
print(df2.reset_index(drop=True))