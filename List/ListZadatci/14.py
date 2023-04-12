#14.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
#najbolji i najlošiji rezultat.


broj_natjecatelja=int(input("Broj plesnih natjecatelja: "))
ocjene_natjecatelja=[]
counter=0

while counter<broj_natjecatelja:
    ocjena_natjecatelja=int(input("Unesite ocjenu: "))
    ocjene_natjecatelja.insert(0,ocjena_natjecatelja)
    
    counter+=1
    
ocjene_natjecatelja.sort()
#print(ocjene_natjecatelja)

zbroj=sum(ocjene_natjecatelja)
print(zbroj-min(ocjene_natjecatelja)-max(ocjene_natjecatelja))
    











