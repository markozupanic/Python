#8. Napravi igricu s beskonačnim unosom pokreta (L-Lijevo, R-Desno, U-Gore, D-Dolje), početne koordinate su (0, 0),
#   nakon svakog unosa ispišite trenutnu poziciju.
#   Primjer: (0, 0), Unos: D -> (1, 0) | (1, 0), Unos: R -> (1, 1) | (1, 1), Unos: L -> (0, 1)

counter=1
pozicija_prva=0
pozicija_druga=0
while(counter>0):
    print("L-Lijevo")
    print("R-Desno")
    print("U-Gore")
    print("D-Dolje")
    unos=input("Unesite smjer: ")
    
    #pozicija_prva=0
    #pozicija_druga=0
    
    if(unos=="L"):
        pozicija_prva-=1
        print(f"({pozicija_prva},{pozicija_druga})")
    elif(unos=="R"):
        pozicija_druga+=1
        print(f"({pozicija_prva},{pozicija_druga})")
    elif(unos=="D"):
        pozicija_prva+=1
        print(f"({pozicija_prva},{pozicija_druga})")
    elif(unos=="U"):
        pozicija_druga-=1
        print(f"({pozicija_prva},{pozicija_druga})")
    elif(unos=="0"):
        break
        
    
    
    














