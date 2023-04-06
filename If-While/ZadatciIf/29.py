#29. U varijable a i b spremite dva broja. Ako je jedan od brojeva veÄi od 
#100, a onaj drugi manji od 100, tada ispiÅ¡ite poruku "Jedna je veÄa, a 
#druga je manja od 100.". TakoÄer, ispiÅ¡ite prikladne poruke i za 
#sluÄaj ako su obje vrijednosti veÄe od 100 ili pak za sluÄaj ako su 
#obje vrijednosti manje od 100 te ako su obje vrijednosti jednake 100.

a=int(input("Broj: "))
b=int(input("Broj: "))


if(a>100 and b<100):
    print("Jedan veći od 100,drugi manji od 100")
elif(a<100 and b<100):
    print("Oba manja od 100")
elif(a>100 and b>100):
    print("Oba veči od 100")
else:
    print("Obje su jednake 100")











