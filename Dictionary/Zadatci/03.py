#3. zadan je rjecnik {"ime": "pero", prezime: "perkovic", godine: 42}. koristeci metodu update, 
# izmijenite vrijednosti rjecnika u vlastito ime, prezime i godine, 
# zatim dodajte novi par "spol" sa prikladnom vrijednosti.

rjecnik={"ime": "pero", "prezime": "perkovic", "godine": 42}

rjecnik.update({"ime":"marko","prezime":"županic","godine":23})
print(rjecnik)

print(rjecnik.setdefault("spol"))
rjecnik.update({"spol":"muško"})
print(rjecnik)

#4. koristeci funkciju setdefault(), dohvatite i ispisite ime i prezime iz prethodnog zadatka. 
# koristeci istu funkciju, kreirajte novi par "visina" i pridruzite prikladnu vrijednost.
print(rjecnik.setdefault("ime"))
print(rjecnik.setdefault("prezime"))
rjecnik.setdefault("visina")
rjecnik.update({"visina":190})
print(rjecnik)