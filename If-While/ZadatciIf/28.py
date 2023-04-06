#28. U varijablu r spremite neki broj koji predstavlja radijus kugle. Ako je 
#radijus ispravno upisan (radijus ne moÅ¾e biti negativan), ispiÅ¡ite 
#radijus i volumen kugle, V=4/3*r^3*pi InaÄe, ispiÅ¡ite poruku da je 
#vrijednost u varijabli r neispravna.


r=int(input("Radiju: "))
formula=4/3*(r**3)*3.14
if(r<0):
    print("Varijabla r neispravna")
else:
    print(formula)
    






