#1. Provjeri dali je broj palindrom (isto se čita s lijeva na desno i s desna na lijevo).

broj=input("Unesite broj: ")

palindrom_broja=broj[::-1]

if(broj==palindrom_broja):
    print(f"Broj {broj} je palindrom")
else:
    print(f"Broj {broj} nije palindrom")








