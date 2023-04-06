#15. Program treba korisniku omoguÄiti unos broja bodova od 1-100. Zatim program treba prema
#bodovnoj skali za svaki broj bodova ispisati o kojoj se ocjeni radi. Bodovne pragove je
#potrebno odrediti kao uvjete u elif uvjetovanju prema tablici


broj=int(input("Unesite broj od 1-100: "))

if(broj>=0 and broj<=50):
    print("Ocjena:2")
elif(broj>=51 and broj<=75):
    print("Ocjena:3")
elif(broj>=76 and broj<=89):
    print("Ocjena:4")
elif(broj>=90 and broj<=100):
    print("Ocjena:5")
else:
    print("Upisite pravilne bodove")


