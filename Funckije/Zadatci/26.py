#26. napisi funkciju koja prima listu te ispisuje sve elemente liste koji su djeljivi sa 5 i 7.

def djeljenje():
    brojevi=[45,78,56,14,89,70,25,63,12,35]
    for i in brojevi:
        
        if(i%5==0 and i%7==0):
            print(i)

djeljenje()