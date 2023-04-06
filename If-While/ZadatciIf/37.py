#37. NapiÅ¡i program koji unosi rijeÄ i ispisuje poruku je li upisana rijeÄ muÅ¡kog, Å¾enskog ili srednjeg roda. 
#Ako rijeÄ zavrÅ¡ava na o, ispisat Äe se poruka 'srednji rod', ako rijeÄ zavrÅ¡ava na 'a' ispisat Äe se poruka 
#'Å¾enski rod'. U svim ostalim sluÄajevima ispisat Äe se poruka 'muÅ¡ki rod'.

rijec=input("Unesi riječ: ")

zadnje_slovo=rijec[-1]
#print(zadnje_slovo)

if(zadnje_slovo=="o"):
    print("Srednji rod")
elif(zadnje_slovo=="a"):
    print("Zenski rod")
else:
    print("Muški rod")












