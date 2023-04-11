#5. Napravi igricu pogađanja random generiranog broja. Program treba tražiti unos sve dok broj nije pogođen.
#6. Nadogradite 5. tako da program daje hint svako drugo pogađanje dali je unešeni broj veći ili manji od random generiranog.

import random

broj=random.randint(1,10)

unos=int(input("Unesite random broj:"))

while(broj!=unos):
    unos=int(input("Unesite random broj:"))
    #print(unos)
    if(broj<unos):
        print("Broj je manji")
    elif(broj>unos):
        print("Broj je veči")
    else:
        print(f"Čestitamo broj {unos} je bio točan!")








