import pandas as pd


df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


df.sort_values("Age")
print(df.sort_values("Age"))


df.sort_values("Age",ascending=False,na_position="first")
df.sort_values("Age",ascending=True,inplace=True)
print(df)