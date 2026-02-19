import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


salary_df = df.groupby("Job Title")["Salary"].mean().reset_index()
#print(df.groupby("Job Title")["Salary"].mean())  

salary_df.plot(x="Job Title",y="Salary")
plt.show()





