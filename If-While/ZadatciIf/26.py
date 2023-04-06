#26. Iva i Marko sudjelovali su u kvizu znanja. Svako od njih odgovarao je na tri pitanja i za svako
#pitanje osvojili su 1,2 ili 3 boda. Napisi program koji Äe izracunati koliko bodova su ukupno osvojili
#te tko je pobjedio u kvizu! Osvojene bodove unesi pomocu tipkovnice.

bodovi_iva_prvo=int(input("Prvo pitanje Iva bodovi:"))
bodovi_iva_drugo=int(input("Drugo pitanje Iva bodovi: "))
bodovi_iva_trece=int(input("Treče pitanje Iva bodovi: "))

bodovi_marko_prvo=int(input("Prvo pitanje Marko bodovi:"))
bodovi_marko_drugo=int(input("Drugo pitanje Marko bodovi:"))
bodovi_marko_trece=int(input("Trece pitanje Marko bodovi:"))


ukupno_iva_bodovi=bodovi_iva_prvo+bodovi_iva_drugo+bodovi_iva_trece
ukupno_marko_bodovi=bodovi_marko_prvo+bodovi_marko_drugo+bodovi_marko_trece

if(ukupno_iva_bodovi>ukupno_marko_bodovi):
    print("Iva je pobjedila sa " + str(ukupno_iva_bodovi) + " boda")
elif(ukupno_marko_bodovi>ukupno_iva_bodovi):
    print("Marko je pobjedio " + str(ukupno_marko_bodovi) + " boda")
else:
    print("Nerješeno")
    
















