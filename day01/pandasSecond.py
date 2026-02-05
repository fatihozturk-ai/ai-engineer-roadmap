import pandas as pd

# students = [
#     {"isim":"fatih","age":20,"bmi":23.4},
#     {"isim":"hasan","age":23,"bmi":23.4}
# ]

# df = pd.DataFrame(students)
# print(df)

# calısanlar = {
#     "isim" : ["Batuhan","Fatih","Sema"],
#     "odenen tutar": [400,300,150]
# }

# df = pd.DataFrame(calısanlar)
# print(df)
# print(df["isim"])              # pandas series 
# print(df.iloc[1]["odenen tutar"])         # iloc yeri neyse o . loc değişebiliyor



df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")
print(df)


gender_filter = df["Gender"] == "Male"
print(gender_filter)
print(df[gender_filter])

salary_filter = df["Salary"] == 90000

print(df[salary_filter])

job_filter = df["Job Title"] == "Software Engineer"

print(df[job_filter])


print(df[(df["Job Title"]=="Software Engineer") & (df["Gender"]=="Female")])

# df["Job Title"] == "Senior Manager" 
# df["Education Level"] == "Master's"


print(df [ (df["Job Title"] == "Software Engineer") & (df["Education Level"] == "Master's")]) # and

print(df [ (df["Job Title"] == "Software Engineer") | (df["Education Level"] == "Master's")])  # or


print(df["Job Title"].isin(["Director" , "Marketing Manager" ,"Financial Manager"]))

print(df[df["Job Title"].isin(["Director" , "Marketing Manager" ,"Financial Manager"])]) # içinde olanlar

df.at[0,"Job Title"] = None
df.at[1,"Job Title"] = pd.NA


print(df[df["Job Title"].str.contains("Manager",na=True)])    # job title içersiinde Manager olanları bas

print(df[df["Age"] > 30])

print(df[(df["Age"] >= 30) & (df["Age"] <= 40)])


# import numpy as np

# df.at[3,"Job Title"] = np.nan



# df = pd.read_csv("Salary_Data.csv", sep=",")
# df.to_csv("Salary_Data-Semicolon.csv", sep=";", index=False)          # virgülü noktalı virgüle çevirip düzeltiyor



""" df = pd.read_csv("pandasSecond.csv",sep=";")

df["borc"] = pd.to_numeric(df["borc"])
df["odenen tutar"] = pd.to_numeric(df["odenen tutar"])

df["borc"] = df.iloc[0]["borc"]-df["odenen tutar"]   # yanlış basıyor borcu  .cumsum() yazınca düzeliyor

print(df) """