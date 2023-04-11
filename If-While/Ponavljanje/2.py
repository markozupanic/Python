#2. Napravi program za unos dva broja. Brojeve pretvori u binarni zapis, izračunaj i ispiši njihov zbroj.

broj_prvi=int(input("Unesi broj: "))
broj_drugi=int(input("Unesi broj: "))

broj_prvi_bin=bin(broj_prvi)
print(broj_prvi_bin)

broj_drugi_bin=bin(broj_drugi)
print(broj_drugi_bin)

broj_prvi_bin_to_int=int(broj_prvi_bin[2:],2)
#print(broj_prvi_bin_to_int)

broj_drugi_bin_to_int=int(broj_drugi_bin[2:],2)
#print(broj_drugi_bin_to_int)

zbroj=broj_prvi_bin_to_int+broj_drugi_bin_to_int
print(zbroj)




