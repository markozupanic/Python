#25. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni 
#niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable 
#n manja od broja znakova u nizu. Ako je vrijednost varijable n veća 
#ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to 
#slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz 
#"ACEG".

niz_znakova = input("Unesite niz znakova: ")
n = int(input("Unesite broj n: "))

if n > len(niz_znakova):
    print(f"Greška: {n} je veći od broja znakova u nizu!")
else:
    rezultat = ""
    for i in range(0, len(niz_znakova), n):
        rezultat += niz_znakova[i]
    print("Rezultat: " + rezultat)





















