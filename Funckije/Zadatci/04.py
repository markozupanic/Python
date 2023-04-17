#4. napisi funkciju koja vraca faktorijel nekog broja (npr. 6! = 720).

def faktorijal_broja():
    unos_broja=int(input("Unesite broj: "))
    lista_brojeva=[]
    faktorijal=1
    for i in range(1,unos_broja+1):
        print(i)
        faktorijal*=i
        print(faktorijal)



faktorijal_broja()


