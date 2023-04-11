#18. Napisi program u kojem korisnik unosi brojeve, sve dok ne unese 0. Odmah ispisujte samo
#dvoznamenkaste brojeve.


while(True):
    
    broj=int(input("Unesite broj: "))
    broj=str(broj)
    duzina=len(broj)
    
    if(broj==0):
        break
    elif(duzina==2):
        print(broj)
    else:
        continue
        
        
    
    

    
    





