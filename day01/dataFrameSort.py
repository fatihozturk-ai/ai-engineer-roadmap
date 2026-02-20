import pandas as pd


df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


""" df.sort_values("Age")
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

print(df[df["Gender"] == "Male"])

print(df[df["Gender"] == "Male"].count()) 

print(df["Gender"].value_counts())

print(df["Education Level"].value_counts(normalize=True))    # normalize=True yüzdelik olarak veriyor

 """
print(df.describe())        # ortalama,max,min dataframedeki şeyleri gösteriyor
df["Age"].mean() # yaş kolonu ortalaması

print(df.head(5))

print(df["Age"].value_counts()[27]) # yaşı 27 oalnların sayısı



print(df.groupby("Job Title").size())          # meslekleri GRUPLANDIRIR yanlarınada size'ları
print(df.groupby("Job Title")["Salary"].mean())   # meslekleri GRUPLANDIRIR yanlarına maaş ortalamaları



df["Years of Experience"] = df["Years of Experience"].apply(lambda x : x+10 if x>6 else x)      # lambda x:  o sütundaki değerleri alır
print(df)


print(df.groupby("Education Level").size()) # cinsiyetleri gruplandırıp sayıları veriyor
print(df.groupby("Job Title").apply(lambda x: x[["Salary"]]))  # meslek isimlerini ve maaşları basar çift köşeli parantez
# ama bu satırı kullanmak yerine iki kolonu basmak için direkt df["Job title","Salary"]
