#17. Napisati program koji simulira bacanje novčića n puta te ispisati koliko puta se
#pojavljuje pismo i glava.
import random
bacanje_novcica=int(input("Koliko puta želite bacit novici: "))

strana_novcica=["Pismo","Glava"]
for i in range(bacanje_novcica):
    print(random.choice(strana_novcica))
    
    

    





