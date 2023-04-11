#27. Napisi program koji neku ucitanu rijec s tipkovnice mijenja tako da prvo
#slovo premjesti na kraj i potom na novu rijec doda nastavak -py. Program treba ispisati novu rijec


rijec=input("Unesi riječ: ")
nastavak="-py"
prvo_slovo=rijec[0]
#print(prvo_slovo)
nova_rijec=rijec[1: ]+rijec[0]+nastavak
print(nova_rijec)





