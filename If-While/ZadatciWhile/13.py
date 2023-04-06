#13. Napraviti program koji Äe korisniku omoguÄiti pogaÄanje brojeva. Ako korisnik upiĹĄe bilo
#koji broj, izvrĹĄavati Äe se blok naredbi ispod while petlje. Ako odabere 0, dogodi se prekid
#programa. Prekid programa omoguÄiti sa naredbom break. Ako korisnik upiĹĄe toÄan broj,
#ispiĹĄe se poruka o pogoÄenom broju i program se dalje izvrĹĄava. Ako korisnik napiĹĄe prevelik
#ili premali broj od traĹženog, ispisati prigodnu poruku korisniku i dalje izvrĹĄavati program,
#sve dok korisnik sam ne odabere opciju 0.


while(True):
    broj=int(input("Unesite broj: "))
    if(broj==0):
        print("Pogodili ste")
        break
    elif(broj>0):
        print("Napisali ste prevelik broj!")
    else:
        print("Napisali ste premali broj")














