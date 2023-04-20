#3. kreirajte klasu Vozilo, koja sadrzi sljedece atribute:
# marka, model, masa, kilometraza, max brzina, boja, cijena. 
# napravite 2 objekta sa razlicitim atributima. nakon postavljanja, izmijenite boju u crvenu,
# kilometrazu postavite na 10000, max brzinu spustite za 15km/h i cijenu spustite za 10%. 
# usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu.


from Automobili import Vozilo

toyota=Vozilo("Toyota","Corolla",1800,5000,190,"Bjela",200000)
opel=Vozilo("Opel","Astra",2000,220000,200,"Srebrna",30000)

Vozilo.ispisi_pocetno(toyota)
Vozilo.ispisi_pocetno(opel)








