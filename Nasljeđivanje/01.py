#1. napravite klasu Prva i Druga. neka obje imaju po 2 atributa i po jednu metodu za ispis proizvoljnog teksta. 
# izvedite drugu klasu iz prve te ispisite sva 4 atributa koristeci izvedenu klasu.

class Prva():
    def __init__(self,ime,prezime):
        self.ime=ime
        self.prezime=prezime 
        
    def ispis_prva(self):
        print("ispis prvi")
        


class Druga(Prva):
    def __init__(self,ime,prezime,adresa,telefon):
        Prva.__init__(self,ime,prezime)
        self.adresa=adresa
        self.telefon=telefon
        
    def ispis_druga():
        print("ispis druga")
        
    def ispis_varijabli(self):
        print(f"ime:{self.ime} prezime: {self.prezime} adresa: {self.adresa} telefon:{self.telefon}")



podatci=Druga("marko","županić","a.starčevića 13","098513674")
Druga.ispis_varijabli(self=podatci)
Druga.ispis_druga()


        