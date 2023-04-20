#3. kreirajte klasu Vozilo, koja sadrzi sljedece atribute: 
# marka, model, masa, kilometraza, max brzina, boja, cijena. 
# napravite 2 objekta sa razlicitim atributima. nakon postavljanja, izmijenite boju u crvenu,
# kilometrazu postavite na 10000, max brzinu spustite za 15km/h i cijenu spustite za 10%. 
# usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu.

class Vozilo:
        
    keys=["marka","model","masa","kilometraza","max_brzina","boja","cijena"]
    valus=[]
    
    def __init__(self,marka,model,masa,kilometraza,max_brzina,boja,cijena):
        self.marka=marka
        self.model=model
        self.masa=masa
        self.kilometraza=kilometraza
        self.max_brzina=max_brzina
        self.boja=boja
        self.cijena=cijena
        
    def ispisi_pocetno(self):
        print(f"marka: {self.marka} model: {self.model} masa: {self.masa} kilometraža: {self.kilometraza} max brzina: boja: {self.boja} cijena: {self.cijena}")
    
    def promjenjeni_podatci(self):
        pass




