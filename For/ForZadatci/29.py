#29. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od
#brojeva

koliko_brojeva_unosi=int(input("Koliko brojeva želite unjet: "))

ostat_najveci=[]

lista_brojeva=[]
i=0
#zbroj_stringova=" "


for a in range(0,koliko_brojeva_unosi):
    broj=input("Unesite broj: ")
    for i in range(len(broj)):
      lista_brojeva.append(broj[i])
      lista_brojeva.sort()
      najveci_broj_liste=lista_brojeva[-1]
      #zbroj_stringova=zbroj_stringova+najveci_broj_liste
      i+=1
    ostat_najveci.append(najveci_broj_liste)
    if(lista_brojeva!=0):
      lista_brojeva.clear()
    
b=0
rjesenje=""
for i in range(len(ostat_najveci)):
    rjesenje+=ostat_najveci[b]
    b+=1

#print(lista_brojeva)
print(ostat_najveci)
#print(najveci_broj_liste)
#print(len(ostat_najveci))
print(rjesenje)










