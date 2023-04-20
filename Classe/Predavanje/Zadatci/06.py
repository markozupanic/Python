#6. napravite klasu za ObradaStringa. klasa treba imati mogucnosti da iz nekog stringa napravi sljedece (u obliku metoda):
#a) svaku rijec kapitalizira (prvo pocetno slovo) i spremi u listu
#b) ispisuje broj velikih i malih slova, brojeva, znakova
#c) unazadno ispisuje rijec po rijec (npr ako je uneseno "ja sam" treba ispisati "aj mas")
#d) spajanje rijeci iz liste pod a) u jednu rijec
#e) filtriranje brojeva ili slova, ovisno o trazenom
#napravite objekte, pozovite i testirajte program.

class ObradaStringa:
    
    def kapitaliziranje_prvo_slovo():
        global lista
        lista=[]
        unos_stringa=input("Unesite recenicu: ")
        kapitalizacija=unos_stringa.title()
        lista.append(kapitalizacija)
        print(lista)
        
    def broj_velikih_malih_brojeva_znakova():
        unos_stringa=input("Unesite rečenicu: ")
        veliko_slovo=0
        malo_slovo=0
        broj=0
        znak=0
        
        for i in unos_stringa:
          if(i.islower()):
            malo_slovo=malo_slovo+1
          elif(i.isupper()):
            veliko_slovo=veliko_slovo+1
          elif(i.isnumeric()):
            broj=broj+1
          else:
            znak=znak+1
        
        print(f"velika slova: {veliko_slovo} | malo slovo: {malo_slovo} | broj: {broj} | znak: {znak}")
        
    def unazad_rijec_po_rjec():
        recenica=" "
        za_ubacit=[]
        unos_stringa=input("Unesite rečenicu: ")
        rijeci=unos_stringa.split()
        for i in rijeci:
            okrenuta_rijec=i[::-1]
            za_ubacit.append(okrenuta_rijec)
        for i in za_ubacit:
            recenica+= " "+i
        print(recenica)
            
            
            
    
        
            
        

ObradaStringa.kapitaliziranje_prvo_slovo()
ObradaStringa.broj_velikih_malih_brojeva_znakova()
ObradaStringa.unazad_rijec_po_rjec()














