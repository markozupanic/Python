#3. napisi funkciju koja prima tri vrijednosti i vraca najvecu vrijednost brojeva te ispisuje koji su od njih parni, a koji neparni.


def funkcija():
    lista_brojeva=[]
    for i in range(3):
        unos_broja=int(input("Unesite broj: "))
        lista_brojeva.append(unos_broja)
        
        if(unos_broja%2==0):
            print(f"Uneseni {unos_broja} broj je paran")
        else:
            print(f"Uneseni broj {unos_broja} je naparan")    
            
    lista_brojeva.sort()
    print(f"Broj {lista_brojeva[-1]} je največi od 3 broja")
    
funkcija()
        





































