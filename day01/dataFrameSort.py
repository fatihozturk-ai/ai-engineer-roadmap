import pandas as pd


df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


df.sort_values("Age")
#print(df.sort_values("Age"))


df.sort_values("Age",ascending=False)
df.sort_values("Age",ascending=True) 
#print(df)

print(df.sort_values(["Age","Salary"],ascending=[True,False]))   # önce age sonra salary

df = df.sort_index()
print("-------------")
print(df)

df2 = df.nlargest(10,"Salary")
print(df2)

df3 = df.nsmallest(10,"Salary")
print(df3)

print(df2.reset_index())
print(df2.reset_index(drop=True))

print(df.head(15))
print(df.describe())

print(df[df["Gender"] == "Male"]["Gender"].count()) 

print(df["Gender"].value_counts())

print(df["Education Level"].value_counts(normalize=True))    # normalize=True yüzdelik olarak veriyor