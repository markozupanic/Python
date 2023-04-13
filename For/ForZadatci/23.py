#23. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
#(stupac) i y (redak) neka budu manje od 10. Program neka ispiše 
#polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
#je vrijednost "X"

x=int(input("Unesite x točku: "))
y=int(input("Unesite y točku: "))

for redak in range(10):
        for stupac in range(10):
            if redak == y and stupac == x:
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()

















