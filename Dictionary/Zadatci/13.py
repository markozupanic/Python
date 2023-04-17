#16. Napravite hrvatsko-engleski rjeÃÂnik. KljuÃÂ podataka neka bude hrvatska rijeÃÂ,
# a vrijednost toga kljuÃÂa neka bude engleska rijeÃÂ. Napuniti rjeÃÂnik s 5 elemenata.
# Napraviti beskonaÃÂnu petlju koja uÃÂitava s tipkovnice hrvatske rijeÃÂi.
# Za svaku uÃÂitanu rijeÃÂ (ako prijevod postoji) ispisati prijevod, a ako traÃÂ¾ena rijeÃÂ ne postoji,
# ispisati poruku da ta rijeÃÂ ne postoji u rjeÃÂniku. UÃÂitavanje raditi tako dugo dok se ne unese znak 'x'.
# Potrebno je obratiti paÃÂ¾nju na mala/velika slova. Prijedlog je pretvarati sve u mala slova.

rijeci={"ime":"name","prezime":"surname","grad":"city","spol":"gender","godine":"age"}
rijeci_na_engleskom=rijeci.values()
rijeci_na_hrvatskom=list(rijeci)
rijeci_na_engleskom_list=list(rijeci_na_engleskom)
print(rijeci_na_hrvatskom)
print(rijeci_na_engleskom_list)

for i in rijeci_na_engleskom_list:
    unos_rijeci=input("Unesite rijec: ")
    if(unos_rijeci==rijeci_na_hrvatskom[i]):
        print(rijeci_na_engleskom_list[i])
    elif(unos_rijeci=="x"):
        break
    else:
        print("Unesite ponovo")
        
    

    
    









