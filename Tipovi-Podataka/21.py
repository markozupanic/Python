#21. Vlatka je dobila od bake x kuna i odlucila kupiti cokoladice. Svaka cokoladica kosta y kuna.
#Napisi program koji ce ucitati koliko je kuna Vlatka dobila i cijenu svake cokoladice te ispisati u
#dva retka koliko Vlatka moze kupiti cokoladica za svoj novac i koliko joj je kuna ostalo kad kupi cokoladice.

vlatka_novci=int(input("Vlatka dobila: "))
cijena_cokoladice=int(input("CIjena cokoladice: "))

broj_kupljenih_cokoladica=vlatka_novci//cijena_cokoladice
print(broj_kupljenih_cokoladica)

ostatak=vlatka_novci-(cijena_cokoladice*broj_kupljenih_cokoladica)
print(ostatak)