#16. napisi funkciju koja prima sekvencu rijeci odvojenu zarezom. 
# funkcija ispisuje alfabetski sortiran string (npr. "marko, ivan, pero" => "ivan, marko, pero")

def poredat_po_abecedi():
    lista_rijeci=[]
    for i in range(3):
        unos_rijeci=input("Unesite riječ: ")
        lista_rijeci.append(unos_rijeci)
        
    sortirana_lista=sorted(lista_rijeci)
    print(sortirana_lista)
    

        



poredat_po_abecedi()






















