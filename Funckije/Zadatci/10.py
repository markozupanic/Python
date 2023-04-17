#10. napisi funkciju koja prima string i racuna broj upper case, lower case slova te brojeva. formatiraj ispis po zelji.

def racuna_lower_upper_br_slova():
    unos=input("Unesite: ")
    velika_slova=0
    mala_slova=0
    brojevi=0
    for i in range(len(unos)):
        if(unos[i].isupper()):
            velika_slova+=1
        elif(unos[i].islower()):
            mala_slova+=1
        else:
            brojevi+=1
    
    print(velika_slova)
    print(mala_slova)
    print(brojevi)        
   

racuna_lower_upper_br_slova()






























