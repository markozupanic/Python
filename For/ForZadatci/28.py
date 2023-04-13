#28. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj.


koliko_brojeva_unosi=int(input("Koliko brojeva želite unjet: "))

novi_broj=""

for i in range(koliko_brojeva_unosi):
    unesen_broj=input("Unesite broj: ")
    novi_broj+=unesen_broj[-2]
    
print(novi_broj)





