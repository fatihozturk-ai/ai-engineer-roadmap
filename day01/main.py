""" x=3
y=5

print("toplamı: " , x+y)

print("5 + 6 = " , 5+6)
print("5 * 6 = " , 5*6)



age = 25 
name = "FAtti"
height = 1.75 

print("age: ",age)
print("name:",name) 


year = 2026

birthyear = 2026-age 
print("birthyear is ",birthyear)


name = input("ismini gir")
age = int(input("yaşını gir"))

print(name)
print("doğum yılı = ",year-age)

if age >= 18 :
    print("Reşitsin")
else:
    print("Reşit değilsin")


boy = float(input("boyunuzu girin"))
kilo = float(input("kilonuzu girin"))

bmi = kilo / (boy*boy) 

if bmi > 25 :
    print("Fazla Kilo")
elif bmi>=18.5 :
    print("normal")
else:
    print("zayıf")


print(bmi)
print(f"bmi = {bmi:.2f}") """

# def bmi_hesapla(boy_cm,kilo):
#     boy_m = boy_cm/100
#     return kilo/(boy_m*boy_m)

""" print(bmi_hesapla(175,75))
print(f"{bmi_hesapla(175,75):.2f}")

while True :
    boy = float(input("boy(cm): ?"))
    kilo = float(input("kilo(kg) ?"))
    bmi = bmi_hesapla(boy,kilo)

    if bmi>25: 
        print("yüksek")
    elif bmi>18.5:
        print("normal")
    else:
        print("düşük")
    
    devam = input("devam edilsin mi ? (e/h)")
    if devam == "h" :
        break 
 """
""" def bmi_durum(bmi):
    if bmi > 25 :
        print("yüksek")
    elif bmi>=18.5 :
        print("normal")
    else:
        print("düşük")
 """
""" def bmi_durum(bmi):
    if bmi > 25 :
        return "yüksek"
    elif bmi>=18.5 :
        return "normal"
    else:
        return "düşük"

bmi = 23
print("Durum :", bmi_durum(bmi)) """

# print("DAY 5-------------------")

# bmi_list = [15.5,16.5,24,27.2]
# print(bmi_list,"---------")


# for i in bmi_list:
#     print(i)

# def bmi_durum(bmi) :
#     if bmi>25 :
#         return "yüksek"
#     elif bmi>18.5 :
#         return "normal"
#     else :
#         return "düşük"

# for i in bmi_list :
#     print(i,"-->",bmi_durum(i))


# toplam = 0

# for i in bmi_list :
#     toplam += i 

# ortalama = toplam / len(bmi_list)
# print("ortalama : " , round(ortalama,2))

# #Dictionary

# user = {
#     "name" : "Fatih" ,
#     "age" : 27 ,
#     "weight" : 75
# }

# print(user["name"])
# print(user["age"])


# users = [
#     {"name":"fatih","bmi":22.4},
#     {"name":"zeynep","bmi":15.3},
#     {"name":"hasan","bmi":8.5}
# ]

# for u in users :
#     print(u["name"] , "->",u["bmi"],bmi_durum(u["bmi"]))


# people = [
#     {"name":"A","weight":75,"height":1.8},
#     {"name":"B","weight":100,"height":1.95},
# ]



# for p in people :
#     bmi = bmi_hesapla(p["height"],p["weight"])
#     print(p["name"],"->",f"{bmi:.2f}","-",bmi_durum(bmi))


# vib_banko = [
#     {"name": "batuhan","age" : 30 , "position" : "junior"},
#     {"name": "fatih","age" : 25 , "position" : "senior"}
# ]

# for b in vib_banko :
#     print(b["name"] , "->" , b["position"])

# def bmi_hesapla(boy,kilo) :
#     return kilo / (boy*boy) 


# def bmi_durum(bmi) :
#     if bmi>25 :
#         return "yüksek"
#     elif bmi>=18.5 :
#         return "normal"
#     else :
#         return "düşük"



# import csv
# people = [] 

# with open("people.csv",newline="") as file :
#     reader = csv.DictReader(file)
#     for row in reader :
#         row["height"] = float(row["height"])
#         row["weight"] = float(row["weight"])
#         people.append(row)

# print(people)

# for p in people :
#     bmi = bmi_hesapla(p["height"],p["weight"])
#     print(p["name"],"->",f"{bmi:.2f}")

# toplam = 0
# for p in people :
#     toplam += bmi_hesapla(p["height"],p["weight"])

# ortalama = toplam / len(people)
# print(f"Ortalama : {ortalama:.2f}")


import csv 

members = []

with open("gym.csv",newline="") as file :
    reader = csv.DictReader(file)
    for row in reader :
        row["odenen tutar"] = float(row["odenen tutar"])
        members.append(row)

for m in members :
    print(m["isim"],"->",m["odenen tutar"])
    