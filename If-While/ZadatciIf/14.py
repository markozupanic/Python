#14. Napravite program koji Äe za unos dva broja vrÅ¡iti sljedeÄe operacije: zbrajanje,
#oduzimanje, mnoÅ¾enje i dijeljenje.
#Na poÄetku je potrebno korisniku omoguÄiti unos dva broja, zatim odabrati operaciju
#odabirom znaka te operacije (+,-,*,/)

unos=input("Unesite znak: ")
if(unos=="+"):
    a=int(input("Unesi a: "))
    b=int(input("Unesi b: "))
    print(a+b)
elif(unos=="-"):
    a=int(input("Unesi a: "))
    b=int(input("Unesi b: "))
    print(a-b)
elif(unos=="*"):
    a=int(input("Unesi a: "))
    b=int(input("Unesi b: "))
    print(a*b)
elif(unos=="/"):
    a=int(input("Unesi a: "))
    b=int(input("Unesi b: "))
    print(a/b)
else:
    print("Pokusajte ponovo")
    












