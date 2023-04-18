#6. iz prethodnog zadatka pronadji i ispisi najduzu rijec 
# # (ili sve najduze rijeci ukoliko su istih duljina).

FILE_PATH="brojevi.txt"

def ispis_najduze_rijeci():
    
    f=open(FILE_PATH,"r")
    a=f.readlines()
    sortirana_lista=sorted(a,key=len)
    
    najveci_string=len(sortirana_lista[-1])
    
    for i in range(len(sortirana_lista)):
        #print(len(sortirana_lista[i]))
        if(len(sortirana_lista[i])==len(sortirana_lista[-1])):
            print(sortirana_lista[i],end="")
    f.close()


ispis_najduze_rijeci()






















