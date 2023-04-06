#32. U varijable a, b, c, d, e spremite pet razliÄitih brojeva. Ako su bar tri 
#od pet brojeva veÄi od 100, tada ispiÅ¡ite poruku "Zadovoljava.", u 
#suprotnom ispiÅ¡ite poruku "Ne zadovoljava.".

a=int(input("Broj a: "))
b=int(input("Broj b: "))
c=int(input("Broj c: "))
d=int(input("Broj d: "))
e=int(input("Broj e: "))

kombinacija1=a>100 and b>100 and c>100
kombinacija2=a>100 and b>100 and d>100
kombinacija3=a>100 and b>100 and e>100
kombinacija4=b>100 and c>100 and d>100
kombinacija5=b>100 and c>100 and e>100
kombinacija6=c>100 and d>100 and e>100
kombinacija7=d>100 and e>100 and a>100
kombinacija8=e>100 and a>100 and b>100
kombinacija9=a>100 and c>100 and d>100

if(kombinacija1 or kombinacija2 or kombinacija3 or kombinacija4 or kombinacija5 or kombinacija6 or kombinacija7 or kombinacija8 or kombinacija9):
    print("ZAdovoljava")
else:
    print("Nezadovoljava")

















