#15. Ivica ima n kuna za koje Å¾eli kupiti prijateljima Äokolade. Jedna Äokolada stoji m kuna. Ivicu 
#zanima koliko Äe najviÅ¡e Äokolada moÄi kupiti te koliko Äe mu novca nakon toga preostati. 
#Pomogni Ivici i napiÅ¡i program koji Äe unositi iznos novca kojim Ivica raspolaÅ¾e te cijenu jedne 
#Äokolade, a ispisivati koliko maksimalno Äokolada Ivica moÅ¾e kupiti te koliko Äe mu novca 
#nakon toga ostati. 

ivicin_novac=int(input("Ivicin novac: "))
cijena_cokolade=int(input("CIjena cokolade: "))

maksimalno_cokolada=ivicin_novac//cijena_cokolade
print(maksimalno_cokolada)

ostatak=ivicin_novac-(cijena_cokolade*maksimalno_cokolada)
print(ostatak)