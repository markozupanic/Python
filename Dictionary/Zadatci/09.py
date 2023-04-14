#11. napisite program koji bi trazio unos po 2 vrijednosti u dva rjecnika, spojio ih te ispisao spojeni rjecnik

dict_1={}
dict_2={}


for i in range(2):
    unos_kljuca=input("Unesite kljuc: ")
    unos=input("Unesite varijablu: ")
    dict_1.setdefault(unos_kljuca)
    dict_1.update({unos_kljuca:unos})
print(dict_1)
for i in range(2):
    unos_kljuca=input("Unesite kljuc: ")
    unos=input("Unesite varijablu: ")
    dict_2.setdefault(unos_kljuca)
    dict_2.update({unos_kljuca:unos})
print(dict_2) 

dict_1.update(dict_2)
print(dict_1)

    











