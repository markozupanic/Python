#3. kreirajte klasu Vozilo, koja sadrzi sljedece atribute:
# marka, model, masa, kilometraza, max brzina, boja, cijena. 
# napravite 2 objekta sa razlicitim atributima. nakon postavljanja, izmijenite boju u crvenu,
# kilometrazu postavite na 10000, max brzinu spustite za 15km/h i cijenu spustite za 10%. 
# usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu.


class Vozilo:

    def __init__(self, marka, model, masa, kilometraza, max_brzina, boja, cijena):
        self.marka = marka
        self.model = model
        self.masa = masa
        self.kilometraza = kilometraza
        self.max_brzina = max_brzina
        self.boja = boja
        self.cijena = cijena
        

    def ispis_atributa(self):
        print("Marka auta je: " + str(self.marka))
        print("Model auta je: " + str(self.model))
        print("Masa auta je: " + str(self.masa))
        print("Kilometraza auta je: " + str(self.kilometraza))
        print("Maksimalna brzina auta je: " + str(self.max_brzina))
        print("Boja auta je: " + str(self.boja))
        print("Cijena auta je: " + str(self.cijena))


njemacko_auto = Vozilo("Audi", "R8", 1400, 50000, 300, "Crni", 35000)
njemacko_auto.boja = "Crveni"
njemacko_auto.kilometraza = 10000
njemacko_auto.max_brzina -= 15
njemacko_auto.cijena = njemacko_auto.cijena - (njemacko_auto.cijena * (10/100))
njemacko_auto.ispis_atributa()

print("\n")

japansko_auto = Vozilo ("Honda", "Accord", 1100, 80000, 260, "Crvena", 20000)
japansko_auto.boja = "Crveni"
japansko_auto.kilometraza = 10000
japansko_auto.max_brzina -= 15
japansko_cijena = japansko_auto.cijena - (japansko_auto.cijena * (10/100))
japansko_auto.ispis_atributa()

# usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu
print("\n")

def usporedba_brzine():
    if njemacko_auto.max_brzina > japansko_auto.max_brzina:
        print("Njemačko auto je brže!")
    elif njemacko_auto.max_brzina < japansko_auto.max_brzina:
        print("Japansko auto je brže!")
    else:
        print("Brzine su jednake!")

def usporedba_kilometraze():    
    if njemacko_auto.kilometraza > japansko_auto.kilometraza:
        print("Njemačko ima više prijeđenih kilometara!")
    elif njemacko_auto.kilometraza < japansko_auto.kilometraza:
        print("Japansko ima više prijeđenih kilometara!")
    else:
        print("Auti imaju jednako kilometara!")
    
def usporedba_cijene():     
    if njemacko_auto.cijena > japansko_auto.cijena:
        print("Njemačko auto je skuplje!")
    elif njemacko_auto.cijena < japansko_auto.cijena:
        print("Japansko auto je skuplje!")
    else:
        print("Cijene su jednake!")
        


usporedba_brzine()
usporedba_kilometraze()
usporedba_cijene()







