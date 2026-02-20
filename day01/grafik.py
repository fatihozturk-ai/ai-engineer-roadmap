import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data_Semicolon.csv",sep=";")


salary_df = df.groupby("Job Title")["Salary"].mean().reset_index() 
print(salary_df)
print(salary_df.sort_values("Salary",ascending=False))   

salary_df.head(5).plot(x="Job Title",y="Salary",kind="barh")   # plot içerisindeki kind="barh" x eksenini y yapar
plt.show()





