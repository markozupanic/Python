#5. â¢ Unesite 2 broja
#   â¢ Ako su oba broja jednaka izraÄunati povrÅ¡inu kvadrata (p=a**2)
#   â¢ U suprotnom izraÄunati povrÅ¡inu pravokutnika (a*b)


broj_a=int(input("Upiši broj: "))
broj_b=int(input("Upiši broj: "))

povrsina_kvadrata=broj_a**2
povrsina_pravokutnika=broj_a*broj_b

if(broj_a==broj_b):
    print(povrsina_kvadrata)
else:
    print(povrsina_pravokutnika)



