#5. kopirajte rjecnik iz prethodnog zadatka, uklonite posljednji unos, a zatim uklonite "spol". ispisite rjecnik
#6. koristeci for petlju, ispisite rjecnik (oba nacina)
rjecnik={"ime": "pero", "prezime": "perkovic", "godine": 42,"spol":"muško","visina":190}

for rjec in rjecnik:
    print(rjec)



rjecnik.pop("visina")
rjecnik.pop("spol")
print(rjecnik)











