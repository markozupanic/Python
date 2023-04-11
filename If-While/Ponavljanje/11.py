#10. Za unesena dva broja ispiši sve brojeve između njih.
#   Primjer: 4, 8 -> 5, 6, 7
#11. Zadatak iznad nadogradi tako da ipiše samo proste brojeve. Prosti brojevi su djeljivi samo s 1 i samim sobom.

broj_jedan=int(input("Unesite broj: "))
broj_dva=int(input("Unesite broj: "))
broj=0

while(broj_jedan<(broj_dva-1)):
    broj_jedan+=1
    broj+=1
    if(broj_jedan==2):
        print(broj_jedan)
    elif(broj_jedan==3):
        print(broj_jedan)
    elif(broj_jedan==5):
        print(broj_jedan)
    elif(broj_jedan==7):
        print(broj_jedan)
    elif(broj_jedan==11):
        print(broj_jedan)
    elif((6*(broj)+1)==broj_jedan):
        print(broj_jedan)
    








