#8. NapiÅ¡ite program u kojem su navedene varijable a=5, b=10, 
#c=15, d=21. Program mora vratiti aritmetiÄku sredinu danih 
#brojeva. Rezultat spremite u varijablu jer Äe se vrijednost koristiti i u 
#sljedeÄem zadatku. AritmetiÄka sredina raÄuna se tako da se sve 
#dane vrijednosti zbroje te se rezultat podijeli s brojem varijabli.

#Iskoristite prethodni zadatak te dobiveni rezultat pretvorite u cijeli broj
#i tu vrijednost spremite u varijablu. Nad cjelobrojnom aritmetiÄkom 
#sredinom koju ste prethodno spremili u varijablu napravite
#kvadriranje i ispiÅ¡ite dobiveni rezultat.

#10. KoriÅ¡tenjem skraÄenih aritmetiÄkih operatora rezultat dobiven iz 
#prethodnog zadatka pomnoÅ¾ite sa 100 i ispiÅ¡ite dobivenu vrijednost.

#PomoÄu operatora usporedbe provjerite je li broj koji ste dobili u 
#prethodnom zadatku manji od 500. IspiÅ¡ite rezultat usporedbe (ispis 
#Äe biti vrijednosti "True" ili "False").

a=5
b=10
c=15
d=21

aritmetika_sredina=(a+b+c+d)/4
print(aritmetika_sredina)

cjeli_broj_aritmetike_sredine=round(aritmetika_sredina)
print(cjeli_broj_aritmetike_sredine)
kvadriranje=cjeli_broj_aritmetike_sredine**2
print(kvadriranje)

množenje_sa_sto=kvadriranje*100
print(množenje_sa_sto)

usporedba=množenje_sa_sto<500
print(usporedba)