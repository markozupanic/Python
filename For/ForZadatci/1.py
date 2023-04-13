#1. Napiši program koji unosi riječ i ispisuje samo samoglasnike
#1a. Prosiri prethodni program tako da umjesto samoglasnika program prebroji i ispise broj
#samoglasnika u rijeci.
#1b. Prosiri prethodni program tako da ispisuje broj samoglasnika, broj suglasnika i broj svih


samoglasnici=[]
samoglasnici_broj=0
ostali_znakovi=0
rijec=input("Unesite rijec: ")
slovo_rijeci=0
for i in range(len(rijec)):
    if(rijec[slovo_rijeci]=="a"):
        samoglasnici.append("a")
        samoglasnici_broj+=1
        ostali_znakovi+=1
        print("a")
    elif(rijec[slovo_rijeci]=="e"):
        samoglasnici.append("e")
        samoglasnici_broj+=1
        ostali_znakovi+=1
        print("e")
    elif(rijec[slovo_rijeci]=="i"):
        samoglasnici_broj+=1
        ostali_znakovi+=1
        samoglasnici.append("i")
        print("i")
    elif(rijec[slovo_rijeci]=="o"):
        samoglasnici_broj+=1
        ostali_znakovi+=1
        samoglasnici.append("o")
        print("o")
    elif(rijec[slovo_rijeci]=="u"):
        samoglasnici_broj+=1
        ostali_znakovi+=1
        samoglasnici.append("u")
        print("u")
    else:
        ostali_znakovi+=1

    slovo_rijeci+=1
print(samoglasnici)
print(samoglasnici_broj)
print(ostali_znakovi) 


















