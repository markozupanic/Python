#9. napravite klasu Banka. definirajte atribute korisnika u obliku rjecnika 
# (oib, ime, prezime, stanje racuna, mjesecni prihod, ima li osiguranje). 
# napravite metodu za podizanje kredita. metoda mora provjeriti da li je stanje racuna pozitivno, 
# jesu li mjesecni prihodi visi od 5% od ukupne trazene svote kredite. ukoliko jesu, metoda vraca True.
# napravite metodu koja bi izracunala koliko bi mjeseci (i godina) bilo potrebno da korisnik vrati novac.
# nadogradite program tako da racuna i kamate na godisnjoj razini te ispisite rezultat.

class Banka:
    
    def __init__(self,oib,ime,prezime,stanje_racuna,mjesecni_prihod,osiguranje):
        self.oib=oib
        self.ime=ime
        self.prezime=prezime
        self.stanje_racuna=stanje_racuna
        self.mjesecni_prihodi=mjesecni_prihod
        self.osiguranje=osiguranje
        
        keys=["oib","ime","prezime","stanje_racuna","mjesecni_prihod","osiguranje"]
        values=[oib,ime,prezime,stanje_racuna,mjesecni_prihod,osiguranje]
        
        banka_dict=dict(zip(keys,values))
        return banka_dict
    
        
klijent_prvi=Banka(1568484153,"Marko","Županić",500,1500,True)






























