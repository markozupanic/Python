#26. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz 
#znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
#unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti 
#i ispisati informaciju da je veliko slovo "A" pronađeno.


varijabla_znakova=input("Unesite znakove: ")
velika_slova=0

for i in range(0,len(varijabla_znakova)):
    
    if(varijabla_znakova[i].isupper()==True):
        velika_slova+=1
    
    if(varijabla_znakova[i]=="A"):
        print("Veliko slovo A je pronađeno")
        break
        
print(velika_slova)













