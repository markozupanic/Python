#36.  NapiÅ¡i program koji unosi rijeÄ i ispisuje poruku 'Pozdrav!' ako rijeÄ zavrÅ¡ava na 'ka'. U protivnom Äe 
#se ispisati poruka 'Dalje'.

rijec=input("Unesi riječ: ")
rijec_duzina=len(rijec)-2
zadnja_dva_slova_rijeci=rijec[rijec_duzina:]
#print(zadnja_dva_slova_rijeci)

if(zadnja_dva_slova_rijeci=="ka"):
    print("zadovoljava")
else:
    print("Dalje")










