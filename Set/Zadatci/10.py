#11. zadani su skupovi:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
#ispitaj da li je jedan skup podskup drugome, odnosno nadskup drugome.

if x&y==y:
    print("Skup x je nadskup skupa y")
elif y&x==y:
    print("Skup y je nadskup skpa x")
else:
    print("NIjedno")
    
    