#23. napisi program koji racuna iznos racuna u ovisnosti o transakcijama.
# dnevnik transakcija prikazi ovako (D: 100, W: 200), dok ukupan iznos na racunu prikazuje sa (T: 1000). 
# ako korisnik unese T = 1000 te povuce iznos od 350 (W: 350), aplikacija treba ispisati azurirano stanje T: 650.
# ako nakon toga korisnik uplati iznos na racun, npr. 200 (D: 200), program treba uvecati iznos racuna i azurirati ga (T: 850).
# unosom stringa "quit", program prekida se izvodjenje programa.

def ovisnost_o_transakcijama():
    print("1.Trenutno stanje")
    print("2.Uplata")
    print("3.Isplata")
    print("4.Izlaz")
    trenutno_stanje_racuna=500
    while True:
      biranje_mogucnosti=int(input("Koju opciju želite: "))
      if(biranje_mogucnosti==1):
          print(f"Trenutno stanje računa: {trenutno_stanje_racuna} kn")
      elif(biranje_mogucnosti==2):
          iznos_uplate=int(input("Koliko novca bi htjeli uplatit: "))
          trenutno_stanje_racuna+=iznos_uplate
          print(f"Trenutno stanje računa: {trenutno_stanje_racuna} kn")
      elif(biranje_mogucnosti==3):
          iznos_isplate=int(input("Koliko novca želite podići: "))
          trenutno_stanje_racuna-=iznos_isplate
          print(f"Trenutno stanje računa: {trenutno_stanje_racuna} kn")
      elif(biranje_mogucnosti==4):
          break


ovisnost_o_transakcijama()

















