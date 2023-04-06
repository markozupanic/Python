#10. â¢ Unesite dva broja
 #   â¢ Ispitati sljedeÄi logiÄki izraz
  #  â¢ a>0 and b<a
  #  â¢ Ako je prethodni izraz ispravan
 #   â¢ Ispisati TRUE te provjeriti sljedeÄi
 #   â¢ logiÄki izraz a>b or b>0
 #   â¢ u suprotnom ispisati FALSE
 #   â¢ Ako je prethodni izraz ispravan
 #   â¢ Ispisati TRUE
 #   â¢ u suprotnom FALSE
 
 
broj_jedan=int(input("Unesite broj: "))
broj_dva=int(input("Unesite broj: "))

if(broj_jedan>0 and broj_dva<broj_jedan):
    print("True")
    if(broj_jedan>broj_dva or broj_dva>0):
        print("True")
    else:
      print("False")
else:
      print("False")      
 
 
 
 
 
 
 
 
 
 
 
 