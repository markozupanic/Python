#14. Program treba traĹžiti od korisnika unos broja u rasponu od 10-20. Ukoliko korisnik pogodi
#raspon; ispisati: cestitamo-unijeli ste broj u rasponu i ispisati broj kojeg je korisnik unio.
#Ako korisnik ne pogodi broj, ispisati: broj nije u rasponu od 10-20; PokuĹĄajte ponovno.
#Petlja se izvrĹĄava tako dugo dok je uvjet na TRUE odnosno dok korisnik unosi brojeve veÄe
#od nula. Ako korisnik unese 0 odnosno FALSE, prekida se izvoÄenje programa.


while(True):
    broj=int(input("Unesite broj od 1-20: "))
    
    if(broj>10 and broj<20):
        print("Čestitamo unjeli ste točan broj:" + str(broj))
        break
    elif(broj==0):
        break
    else:
        print("Broj nije u rasponu")















