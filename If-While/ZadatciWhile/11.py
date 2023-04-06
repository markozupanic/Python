#11. NapiĹĄite program koji ispisuje sumu znamenaka nekog 
#viĹĄeznamenkastog broja. Na primjer, suma broja 159 iznosi 15

broj=input("Upišite broj: ")

while(True):
    duljina_broja=len(broj)
    zadnja_znamenka=str(duljina_broja[-1])
    zbroj=zadnja_znamenka+zadnja_znamenka
    zadnja_znamenka-=1
    print(zadnja_znamenka)






