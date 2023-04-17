#20. napisi funkciju koja prima string i racuna broj slova, brojeva i znakova. formatiraj string koji ispisuje rezultat.
#21. nadogradi prethodni zadatak tako da racuna broj upper case i lower case slova


def racunanje_slova_brojeva_znakova():
    #broj_slova=mala_slova+
    broj_brojeva=0
    broj_znakova=0
    mala_slova=0
    velika_slova=0
    #broj_slova=mala_slova+velika_slova
    
    unos=input("Unesite: ")
    
    for i in unos:
        #print(i)
        if(i.isnumeric()):
           broj_brojeva+=1
        elif(i.islower()):
            mala_slova+=1
        elif(i.isupper()):
            velika_slova+=1
        elif(i.isalpha()):
            broj_slova+=1
        
        else:
            broj_znakova+=1
            
    print(f"broj slova:{mala_slova+velika_slova} broj brojeva:{broj_brojeva} broj malih slova:{mala_slova} broj velikih slova:{velika_slova} broj znakova:{broj_znakova}")




racunanje_slova_brojeva_znakova()












