def to_float(x) :
    x = x.strip()
    if x != "" :
        return float(x)
    else :
        return 0

def oku(dosya_adi) :
    import csv 

    members = []
    with open(dosya_adi,"r",newline="") as file :
        reader = csv.DictReader(file,delimiter=";")
        for row in reader :
            row["kalan borc"] = to_float(row["kalan borc"])
            row["borc"] = to_float(row["borc"])
            row["odenen tutar"] = to_float(row["odenen tutar"])
            members.append(row)
    
    #print(members) 
    return members  


members = oku("modularFunct.csv")

def borcHesap(members) :
    
    toplamBorc = members[0]["borc"]
    for m in members :
        m["kalan borc"] = toplamBorc - m["odenen tutar"]
        toplamBorc = m["kalan borc"]
    
    print(members)

    
borcHesap(members)

def yaz(dosya_adi,members) :
    import csv
    with open(dosya_adi,"w",newline="") as file :
        fieldnames = ["isim","odenen tutar","kalan borc","odenen yer","borc","tarih"]
        writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=";")
        writer.writeheader()
        writer.writerows(members)


yaz("modularFunct-out.csv",members) 


def toplamOdenenTutar(members) :
    total = 0
    for m in members :
        total += m["odenen tutar"]
    return total 

def maxOdenenTutar(members) :
    en_Buyuk = members[0]
    for m in members :
        if m["odenen tutar"] > en_Buyuk["odenen tutar"] :
            en_Buyuk = m
    
    return en_Buyuk

print("toplam odenen tutar: " , toplamOdenenTutar(members))
print("en buyuk odenen tutar: " , maxOdenenTutar(members))