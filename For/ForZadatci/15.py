#15. Omogućite proizvoljan unos brojeva. Zatim unesite te proizvoljne brojeve i ispitajte koliko ih
#ima parnih, a koliko neparnih.

unos_brojeva=int(input("Unesite koliko bi brojeva unjeli: "))
parni_brojevi=0
neparni_brojevi=0

for i in range(unos_brojeva):
    broj=int(input("Unesite broj: "))
    if(broj%2==0):
        parni_brojevi+=1
    else:
        neparni_brojevi+=1
        
print(f"Parni brojevi: {parni_brojevi}")
print(f"Neparni brojevi: {neparni_brojevi}")





