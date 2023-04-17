#18. napisi funkciju koja prima string odvojen prazninama te ispisuje rijeci nakon uklanjanja svih duplikata.


def ukloni_duplicate(string):
    rijeci = string.split()
    
    
    rijeci_bez_duplikata = list(set(rijeci))
    
    
    print("Riječi bez duplikata:")
    for rijec in rijeci_bez_duplikata:
        print(rijec,end=" ")

unos = "ovo je je primjer primjer za za funkciju funkciju string string odvojen odvojen prazninama prazninama"
ukloni_duplicate(unos)

    
















































