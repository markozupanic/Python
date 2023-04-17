#7. zadan je tuple ("marko", "ivan", "pero", "marko", "marko", "marko", "nikola", "ivan", "ivan"). 
# napisi program koji bi prebrojao koliko unesenih imena ima. (npr. ako je korisnik unio "marko", 
# ispisi: "marko se ponavlja u tuple-u 4 puta.")

imena=("marko", "ivan", "pero", "marko", "marko", "marko", "nikola", "ivan", "ivan")
imena=list(imena)
print(imena)
counter=0
unos=input("Unesite ime: ")

for i in imena:
    if(i==unos):
        counter+=1
        
print(f"{unos} se ponavlja {counter} puta u tuple-u")























