#22. Napišite program koji će inicijalizirati varijablu n na proizvoljnu 
#cjelobrojnu vrijednost. Vrijednost varijable n neka predstavlja red 
#tablice. Ispisati tablicu veličine n redaka i n stupaca. Vrijednost 1 
#neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim 
#mjestima. U nastavku slijedi primjer za n=5:

red_stupci=int(input("Unesite broj redova i stupaca:"))

for redak in range(red_stupci):
    for stupac in range(red_stupci):
        print("0 ",end=" ")
        
    print()















