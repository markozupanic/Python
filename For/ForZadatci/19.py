#19.
#• Napišite program koji će unositi broj učenika te omogućiti unos visine učenika
#prema broju unesenih učenika.
#• Program treba ispisati visinu najnižeg i najvišeg učenika

broj_ucenika=int(input("Broj učenika: "))
visine_lista=[]

for i in range(broj_ucenika):
    unos_visine_ucenika=int(input("Visina učenika:"))
    visine_lista.append(unos_visine_ucenika)
    
print(f"Najniži učenik je visok {min(visine_lista)},a najviši učenik je visok {max(visine_lista)}")



