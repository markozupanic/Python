#4. Za uneseni broj izračunaj koliko je potrebno oduzimanja do nule.
#   Pravila: Ako je broj paran podjeli ga sa 2, ako nije oduzmi 1.


broj=int(input("Unesi broj: "))
count=0

while(broj!=0):
   if(broj%2==0):
    broj/=2
    count+=1
    print(broj)
    print(count)
   elif(broj%2==1):
       broj-=1
       count+=1
       print(broj)
       print(count)


        
    









