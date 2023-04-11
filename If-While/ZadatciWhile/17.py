#17. Napisi program koji za ucitani broj n mnozi njegove znamenke sve dok ne dodje do 
# jednoznamenkastog broja. Program treba ispisati koliko puta se mnozenje moze ponoviti.



broj=int(input("Unesite broj: "))

broj=str(broj)
duzina=len(broj)
count=0
množenje=1


while count<duzina-1:
    množenje*=int(broj[count])
    print(množenje)
    count+=1
    











