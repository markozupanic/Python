#35. NapiÅ¡i program koji dopuÅ¡ta unos dvije rijeÄi i ispisuje poruku koja rijeÄ je duÅ¾a

rijec_jedan=input("Unesite riječ: ")
rijec_dva=input("Unesite riječ: ")

rijec_jedan_duzina=len(rijec_jedan)
rijec_dva_duzina=len(rijec_dva)

if(rijec_jedan_duzina>rijec_dva_duzina):
    print(rijec_jedan)
else:
    print(rijec_dva)











