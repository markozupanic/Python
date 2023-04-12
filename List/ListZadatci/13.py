#13.  Napiši program koji upisuje pet brojeva koji predstavljaju rezultate natjecatelja te 
#ispisuje njegov najbolji i najlošiji rezultat.


counter=0
rez=[]
while counter<5:
    input_rez=int(input("Rezultati natjecatelja: "))
    rez.insert(0,input_rez)
    counter+=1

print(f"Najbolji rezultat: {max(rez)}   Najgori rezultat: {min(rez)}")







