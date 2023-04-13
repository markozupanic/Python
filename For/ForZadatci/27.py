#27. Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno 
#djeljivi i s 5 i s 13.


for i in range(1,1000):
    if(i%2==0):
        if(i%5==0 and i%13==0):
          print(i)
    
    
    




