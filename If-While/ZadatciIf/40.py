#40. NapiÅ¡i program koji unosi jednu rijeÄ i provjerava je li ona ima svoju identiÄnu obrnutu verziju.

rijec=input("Napiši riječ: ")
rijec_obrnuta=rijec[::-1]
print(rijec_obrnuta)
if(rijec==rijec_obrnuta):
    input("Ima indentičnu verziju")
else:
    print("Nema indentičnu verziju")








