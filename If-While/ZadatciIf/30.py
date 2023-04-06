#30. U varijable a i b spremite dva broja. Ako je vrijednost varijable a bar 
#za 50 veÄa od vrijednosti varijable b, a uz to je vrijednost varijable b
#parna, tada ispiÅ¡ite poruku "Uvjeti su zadovoljeni.", u suprotnom 
#ispiÅ¡ite poruku "Uvjeti nisu zadovoljeni.".

a=int(input("Broj: "))
b=int(input("Broj: "))

if(a-b>=50 and b%2==0):
    print("Parametri su zadovoljeni")
else:
    print("Parametri nisu zadovoljeni")











