#16. NapiÅ¡ite program koji Äe omoguÄiti unos Å¾eljenog broja. Uneseni broj treba podijeliti sa 3.
#Zatim ako je ostatak dijeljenja s brojem 3 :
#â¢jednak nuli ispisati âplavaâ,
#â¢jednak 1, ispisati âcrvenaâ,
#â¢jednak 2, ispisati âzelenaâ,
#â¢jednak 3, ispisati âljubicastaâ,
#â¢u suprotnom ispisati âzutaâ

broj=int(input("Unesite broj: "))

if(broj%3==0):
    print("plava")
elif(broj%3==1):
    print("crvena")
elif(broj%3==2):
    print("zelena")
elif(broj%3==3):
    print("ljubičasta")
else:
    print("Zuta")








