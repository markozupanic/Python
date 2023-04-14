#10. napravi rjecnik oblika x:x*x. npr. ako je zadan n = 3, ispis treba biti: {1: 1, 2: 4, 3:9}

rjecnik={}

n=int(input("Unesite broj"))
vrijednost=n*n

rjecnik.setdefault(n)
rjecnik.update({n:vrijednost})
print(rjecnik)




