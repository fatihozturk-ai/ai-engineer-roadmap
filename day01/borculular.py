
import csv


members = []

def to_float(x) :
    x = x.strip()
    if x != "" :
        return float(x)
    else :
        return 0


with open("borclular.csv","r",newline="") as file :
    reader = csv.DictReader(file,delimiter=";")
    for row in reader :
        row["borc"] =  float(row["borc"])  if row["borc"] else 0
        members.append(row) 

    print(members)


toplamBorc = 0
for m in members :
    toplamBorc += m["borc"]     

print(toplamBorc)


import csv 



with open("borclular-out.csv","w",newline="") as file :
    fieldnames = ["isim","borc"]
    writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=";")
    writer.writeheader()
    writer.writerows(members)
    
 















    
# import csv


# members = []

# def to_float(x) :
#     return float(x) if x.strip() != 0 else 0


# with open("borclular.csv","r",newline="") as file :
#     reader = csv.DictReader(file,delimiter=";")
#     for row in reader :
#         row["borc"] = to_float(row["borc"])  # if row["borc"] else 0
#         members.append(row) 

#     print(members)