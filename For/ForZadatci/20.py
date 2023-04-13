#20. Napisati program za učitavanje temperature zraka u prethodnih 10 dana te ispisati
#srednju temperaturu iznad nule i srednju temperaturu ispod nule.


#temp_zraka=int(input("Unesite temperaturu zraka: "))
temp_iznad_nule=0
temp_ispod_nule=0
counter_iznad_nule=0
counter_ispod_nule=0
for i in range(10):
    temp_zraka=int(input("Unesite temperaturu zraka: "))
    if(temp_zraka>0):
        temp_iznad_nule=temp_iznad_nule+temp_zraka
        counter_iznad_nule+=1
    else:
        temp_ispod_nule=temp_ispod_nule+temp_zraka
        counter_ispod_nule+=1
        
print(f"Prosječna temperatura iznad 0 je {temp_iznad_nule/counter_iznad_nule}")
print(f"Prosječna temperatura ispod 0 je {temp_ispod_nule/counter_ispod_nule}")  
    




















