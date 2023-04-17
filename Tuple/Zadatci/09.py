#9. zadan je tuple (1, 5, 3, 4, 2). koristeci list comprehension, kvadrirajte elemente iz tuple-a,
# ispisite nakon sortiranja te ga ispisite u obrnutom redosljedu.

brojevi=(1, 5, 3, 4, 2)

brojevi=list(brojevi)
print(brojevi)
counter=0
for i in brojevi:
    print(i)
    brojevi[counter]*=i
    counter+=1
    
brojevi.sort()  
brojevi_unazad=brojevi[::-1]
print(brojevi_unazad)


    





















