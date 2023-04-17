#13. napisi funkciju koja provjerava je li broj prost. prost broj je broj samo ako je djeljiv samo sa 1 i sa samim sobom.


def prosti_broj():
    broj=int(input("Unesite broj: "))
    counter=0
    for i in range(1,broj+1):
        if(broj%i==0):
            counter+=1
    if(counter==2):
     (print("Broj je prost"))
    else:
     print("Broj nije prost")





prosti_broj()









