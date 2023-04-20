#1. napravite klasu Zivotinja. unutar klase definirajte konstruktor koji sadrzi atribute za 
# naziv, tip, masu, vrstu ishrane. definirajte i metodu unutar klase koja ce ispisati navedene atribute,
# zatim kreirajte dva razlicita objekta te pozovite kreiranu metodu.


class Zivotinje:
    def __init__(self,naziv,tip,masa,vrsta_ishrane):
        self.naziv=naziv
        self.tip=tip
        self.masa=masa
        self.vrsta_ishrane=vrsta_ishrane
        
    
    def ispisi_atribute(self):
        print(f"naziv: {self.naziv}\ntip: {self.tip}\nmasa: {self.masa}\nvrsta ishrane: {self.vrsta_ishrane}")
        