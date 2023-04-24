# 9. napravite klasu Banka. definirajte atribute korisnika u obliku rjecnika (oib, ime, prezime, stanje racuna, 
# mjesecni prihod,
# ima li osiguranje). 
# napravite metodu za podizanje kredita. metoda mora provjeriti da li je stanje racuna pozitivno, 
# jesu li mjesecni prihodi visi od 5% od ukupne trazene svote kredite. 
# ukoliko jesu, metoda vraca True. napravite metodu koja bi izracunala koliko bi mjeseci (i godina) 
# bilo potrebno da korisnik vrati novac. nadogradite program tako da 
# racuna i kamate na godisnjoj razini te ispisite rezultat.

#10. nadogradite program iz prethodnog zadatka tako da napravi i konverziju args-a u liste i setove. 
# napravite metodu koja ce 
# vrsiti trazene operacije sa setovima. 
# neka korisnik preko inputa odluci koju operaciju zeli izvrsiti (unija, presjek itd).
        
class Bank():
    def __init__(self,**kwargs):
        self.information = kwargs
        self.createSet()
        print(type(self))
        
       
    def createSet(self):
        self.informationKeys = set()
        self.informationValues = set()
       
        for keys,values in self.information.items():
           self.informationKeys.add(keys)
           self.informationValues.add(values)
           
    def union(self,otherInformation : str):
        if not isinstance(otherInformation,type(self)):
            print("Krivi oblik podataka")
            return
        
        otherInformationValues = otherInformation.informationValues
        union = otherInformationValues.union(self.informationValues)
        intersect = otherInformationValues.intersection(self.informationValues)

        return (union,intersect)
    
        
        
    def raiseCredit(self,iznosKredita):
        if self.information["Stanje"] > 0 and self.information["prihod"] > 0.05 * iznosKredita:
            print("Kredit je odobren")
        else:
            print("Kredit nije odobren")
            
    def timeToPay(self,rataKredita : int ,iznosKredita : int):
        timeToPay = iznosKredita/ rataKredita 
        
        return timeToPay

banka = Bank(OIB=232312313,Ime= "Antonio", Prezime="Kezele", Stanje = 5000, Prihod = 3000, Osiguranje = True)
bankaDva = Bank(OIB=312222222,Ime= "Ivan", Prezime="Kezele", Stanje = 6000, Prihod = 1000, Osiguranje = True)

intersect, union = banka.union()


        




























