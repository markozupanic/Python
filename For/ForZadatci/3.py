#3. Napiši program koji unosi n brojeva i od znamenke desetice svakog broja kreira novi broj. Ispiši novi 
#broj i ispiši umnožak novog broja s 2.

broj_brojeva=int(input("Unesite koliko brojeva želite unjet: "))


for i in range(broj_brojeva):
    broj=int(input("Unesite broj: "))
    a=broj%100
    o=(a%10)
    
    print(f"Novi broj: {(a-o)/10}     Novi broj*2: {((a-o)/10)*2} ")
    
    if(broj<10):
       print("Broj je manji od 10,upišite veći")
















