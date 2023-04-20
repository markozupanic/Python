#2. Ponovno, omogucite unos do trenutka kad je unesen broj -1.
#  Program prvo postavlja pitanje - "zelite li napraviti unos?", ako je odgovor 'da', program se nastavlja, ako je 'ne',
# program se gasi. U slucaju bilo kakvog
#  drugog odgovora, ispisuje se poruka o gresci i trazi novi unos.
#  Ako korisnik zeli napraviti unos, nudi se unos imena, prezimena, broja godina, spola, najdraza zivotinja, najdraza boja.
#  Nakon unosa, program ponovno pita o unosu. Ako je odgovor -1 tokom unosa, prekinuti program i ne dodati uneseno u listu osoba.
#  Kad se program iskljuci, (bilo da je odgovor 'ne' ili je unos u nekom trenutku -1), ispisati sve unesene podatke u redcima.
 
lista_imena=[]
lista_prezimena=[]

while True:
    unos=input("Želite li napraviti unos? ")
    if(unos=="da"):
        unos_ponovo=input("Sigurno želite unjeti podatke?")
        if(unos_ponovo=="da"):
          unos_ime=input("Unesite ime:")
          lista_imena.append(unos_ime)
          unos_prezime=input("Unesite prezime: ")
          lista_prezimena.append(unos_prezime)
        elif(unos_ponovo=="-1"):
            print(f"popis imena: {lista_imena}",end=" | ")
            print(f"popis prezimena: {lista_prezimena}",end=" | ")
            break
        
        
        #itd
    elif(unos=="ne" or unos=="-1"):
         print(f"popis imena: {lista_imena}",end=" | ")
         print(f"popis prezimena: {lista_prezimena}",end=" | ")
         break
   
        
    










