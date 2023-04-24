#7. napisi program koji racuna iznos racuna u ovisnosti o transakcijama. 
# dnevnik transakcija prikazi ovako (D: 100, W: 200), dok ukupan iznos na racunu prikazuje sa (T: 1000).
# ako korisnik unese T = 1000 te povuce iznos od 350 (W: 350), aplikacija treba ispisati azurirano stanje T: 650.
# ako nakon toga korisnik uplati iznos na racun, npr. 200 (D: 200), program treba uvecati iznos racuna
# i azurirati ga (T: 850). unosom stringa "quit", program prekida se izvodjenje programa.

class OvisnostOTransakcijama():
    #def __init__(self,isplata,uplata,trenutno_stanje):
    #    self.isplata=isplata
    #    self.uplata=uplata
    #    self.trenutno_stanje=trenutno_stanje
     
    def upis_podataka(self):
        stanje=0
        while True:
          print("1-Provjera stanja\n2-Uplata:\n3-Isplata\n4-Izlaz")
          mogucnosti=int(input("Odaberite mogučnost: "))
          if(mogucnosti==1):
              print(f"Trenutno stanje računa je: {stanje}")
            
          elif(mogucnosti==2):
            iznos_uplate=int(input("Iznos uplate: "))
            stanje+=iznos_uplate
            print(f"Uplatili ste: {iznos_uplate}")
            print(f"Ostalo vam je još: {stanje}")
          elif(mogucnosti==3):
            iznos_isplate=int(input("Unesite iznos isplate: "))
            stanje-=iznos_isplate
            print(f"Isplatili ste: {iznos_isplate}")
            print(f"Ostalo vam je još: {stanje}")
            
          elif(mogucnosti==4):
            break
        
        
        

        


OvisnostOTransakcijama.upis_podataka(self=0)


















