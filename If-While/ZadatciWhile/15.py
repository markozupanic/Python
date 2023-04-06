#15. Program treba omoguÄiti korisniku odabir jedne od Äetiri aritmetiÄke operacije (+,-,*,/)
#Svakoj operaciji je potrebno dodijeliti neki broj (npr. 1. Zbrajanje, 2. Oduzimanje, 3.
#Mnozenje, 4. Dijeljenje, 5. Izlaz iz programa) Kada korisnik odabere jednu od navedenih
#operacija, od njega se traĹži da unese dva broja. Ispisati rezultat odabrane operacije.


while(True):
    print("zbrajanje")
    print("Oduzimanje")
    print("Množenje")
    print("Djeljenje")
    print("Izlaz")
    znak=input("Unesite opciju: ")
    
    
    if(znak=="zbrajanje"):
        prvi=input("Unesite broj: ")
        drugi=input("Unesite broj: ")
        print(prvi+drugi)
    elif(znak=="Oduzimanje"):
        prvi=input("Unesite broj: ")
        drugi=input("Unesite broj: ")
        print(prvi-drugi)
    elif(znak=="Množenje"):
        prvi=input("Unesite broj: ")
        drugi=input("Unesite broj: ")
        print(prvi*drugi)
    elif(znak=="Djeljenje"):
        prvi=input("Unesite broj: ")
        drugi=input("Unesite broj: ")
        print(prvi/drugi)
    elif(znak=="5.Izlaz"):
        break
    else:
        print("Unesite neki drugi broj")
        
        
        
        
        






