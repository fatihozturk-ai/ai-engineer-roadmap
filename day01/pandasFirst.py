import pandas as pd

#pandas ile dosya okuma
df = pd.read_csv("gym.csv",sep=";")

print(df)

# boş yerleri 0 yazarak temizlemek için
df["odenen tutar"] = pd.to_numeric(df["odenen tutar"],errors="coerce").fillna(0)
df["borc"] = pd.to_numeric(df["borc"],errors="coerce").fillna(0)




df["borc"] = df["borc"].iloc[0] - df["odenen tutar"].cumsum()
df.to_csv("gym-pandas-out.csv",sep=";",index=False)



