#9. napravite klasu Banka. definirajte atribute korisnika u obliku rjecnika 
# (oib, ime, prezime, stanje racuna, mjesecni prihod, ima li osiguranje). 
# napravite metodu za podizanje kredita. metoda mora provjeriti da li je stanje racuna pozitivno, 
# jesu li mjesecni prihodi visi od 5% od ukupne trazene svote kredite. ukoliko jesu, metoda vraca True.
# napravite metodu koja bi izracunala koliko bi mjeseci (i godina) bilo potrebno da korisnik vrati novac.
# nadogradite program tako da racuna i kamate na godisnjoj razini te ispisite rezultat.

class Banka():
    
    def unos_podataka():
        oib=int(input("Unesite oib: "))
        ime=input("Unesite ime:")
        prezime=input("Unesite prezime: ")
        stanje_racuna=int(input("Stanje računa:"))
        mjesecni_prihod=int(input("Mjesečni prihodi:"))
        osiguranje=bool(input("Osiguranje: "))
        
        keys=["oib","ime","prezime","stanje_racuna","mjesecni_prihod","osiguranje"]
        values=[oib,ime,prezime,stanje_racuna,mjesecni_prihod,osiguranje]
        
        banka_dict=dict(zip(keys,values))
        print({banka_dict.values()})
        return banka_dict
    
    def metoda_dizanje_kredita(unos_podataka):
        stanje_racuna=banka_dict.valus(stanje_racuna="")
        
    
    
#Banka.unos_podataka()
        
#klijent_prvi=Banka(1568484153,"Marko","Županić",500,1500,True)






























