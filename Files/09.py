#9. kopiraj i preimenuj datoteku iz prethodnog zadatka. iz navedene datoteke dohvati i izbaci sve duplikate 
# i broj ponavljanja te omogucite korisniku unosenje novog imena ukoliko ono ne postoji u datoteci te ga zapisite u datoteku. npr:
#| 1 | daniel |
#| 3 | mario |
#ce postati:
#daniel

FILE_PATH="stringovi.txt"
def stvara_datoteku():
    f=open(FILE_PATH,"a")
    names = ["ivan", "mario", "julija", "fran", "marko", "jan", "daniel", "ivan", "mario", "mario", "marija", "ana", "ante"]
    unos_imena=input("Unesite ime: ")
    names.append(unos_imena)
    #print(names)
    names_set=set(names)
    names_set=list(names_set)
    #print(names_set)
    
    for i in range(len(names_set)):
        f.write(names_set[i])
        f.write("\n")
    f.close()
    
def ocitanje():
    f=open(FILE_PATH,"r")
    print(f.read())
    
    f.close()



stvara_datoteku()
ocitanje()












