#19. OmoguÄiti korisniku da odabere jednu od 4 aritmetiÄke operacije (+,-,*,/).
#Nakon Å¡to korisnik odabere jednu od operacija, omoguÄiti unos dva broja nad kojima Äe se
#operacija izvrÅ¡iti. Nakon toga ispisati rezultat operacije

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
    



