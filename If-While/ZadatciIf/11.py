#11. Napisati program za mnoÅ¾enje dva broja u rasponu zakljuÄno s brojem 10. Na poÄetku
#programa upitati korisnika da li Å¾eli mnoÅ¾iti brojeve. Ukoliko odgovori pozitivno s da
#omoguÄiti unos i mnoÅ¾enje. Ukoliko odgovori negativno, omoguÄiti izlazak iz programa.
brojevi=""

unos = input("Zelite li mnozit:")
if(unos == "da"):
    a=int(input("Unesite broj"))
    b=int(input("Unesite broj"))
    print(a*b)
    if(a>10 or b>10):
      print("Unjeli ste broj koji je veći od 10 ili manje od 10 ")
    else:
        print(brojevi)
      #print(a*b)

#elif(a>10 and b>10):
# print("Unjeli ste broj koji je veći od 10 ili manje od 10 ")
# print(unos)

else:
    print("Doviđenja")





