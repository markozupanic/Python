#34. NapiÅ¡i program koji unosi ime i ispisuje poruku je li upisano ime muÅ¡ko ili Å¾ensko. Ako ime zavrÅ¡ava na 
#a, ispisat Äe se poruka 'Å½ensko ime', inaÄe Äe se ispisati poruka 'MuÅ¡ko ime.

ime=input("Unesi ime: ")

zadnje_slovo=ime[-1]

if(zadnje_slovo=="a"):
    print("Žensko ime")
else:
    print("Muško ime")









