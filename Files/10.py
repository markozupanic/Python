#10. iz datoteke iz 8. zadatka: napravi program koji ce na korisnikov unos imena formatirati i 
# dodati u novi redak ime ukoliko ono ne postoji u datoteci. ukoliko postoji, samo uveÄaj broj njegovog ponavljanja za 1

from collections import Counter
FILE_PATH="pohranjivanje.txt"

def prebrojavanje_istih():
    f=open(FILE_PATH,"r")
    #print(f.readlines())
    unos=input("Unesite ime: ")
    #a.append(unos+"\n")
    a=f.readlines()
    a.append(unos+"\n")
    print(a)
    c = Counter(a)
    print(c)
    f.close()
    
    
prebrojavanje_istih()













