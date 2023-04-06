#20. OmoguÄiti korisniku unos ocjena od 1-5. Ukoliko korisnik odabere prolaznu ocjenu (2,3,4,5),
#ispisati âocjena ispita je (ocjena rijeÄima), prosli steâ; ako je ocjena negativna ispisati:
#âocjena ispita je nedovoljan, niste prosliâ . Ukoliko korisnik odabere broj koji nije u
#rasponu ocjena, ispisati: âNepostojeca ocjenaâ


ocjena=int(input("Unos ocjene: "))

if(ocjena==2 or ocjena==3 or ocjena==4 or ocjena==5):
    print("Prosli ste")
elif(ocjena==1):
    print("Niste prosli,dobili ste 1")
else:
    print("Nepostoječa ocjena")








