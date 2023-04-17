#2. napisi funkciju koja prima broj ucenika (npr. 1) i vraca da li je ucenik prisutan ili nije. 
# (koristite listu za pohranu ucenika koji su prisutni).
import random

lista_prisutnih=[]

def broj_ucenika():
    unos_broja=int(input("Unesite broj učenika: "))
    l1 = ["yes", "no"]
    for x in range(unos_broja):
      rand = random.randint(0, 1)
      print(l1[rand])
      
    
      if(rand==0):
          lista_prisutnih.append(x)

broj_ucenika()
print(lista_prisutnih)

























