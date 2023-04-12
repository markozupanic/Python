#11. Napisi program koji upisuje rezultat pet najboljih natjecatelja i ispisi koji rezultat je imao
#najbolji natjecatelj te koji je poredu on igrao.

rezultati=[]

index_najboljeg=0
bodovi_najboljeg=0

for index in range(5):
    a=int(input(f"Unesite {index+1} broj bodova: "))
    rezultati.append(a)
    
    if a>bodovi_najboljeg:
        bodovi_najboljeg=a
        index_najboljeg=index_najboljeg+1
        
print(bodovi_najboljeg)
print(index_najboljeg)











