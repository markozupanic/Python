#8. â¢ OmoguÄite dva unosa broja 0 ili 1.
 #  â¢ Upotrijebite operaciju logiÄkog I
  # â¢ Ako je rezultat TRUE ispiÅ¡ite true
   #â¢ U suprotnom ispiÅ¡ite FALSE
   
   
broj_jedan=int(input("Unesite 0 ili 1: "))
broj_dva=int(input("Unesite 0 ili 1: "))



if(broj_jedan==0 and broj_dva==0):
    print("False")
elif(broj_jedan==0 and broj_dva==1):
    print("False")
    
elif(broj_jedan==1 and broj_dva==0):
    print("False")
    
elif(broj_jedan==1 and broj_dva==1):
    print("True")  
else:
    print("Morate upisat 0 ili 1")
    
    
             


   
   
   
   