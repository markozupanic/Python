#10. zadane su liste: 
brojevi = [17, 27, 37] 
slova = ['d', 'f', 'g']
#koristenjem funkcije 'zip' i primjenom 'for' petlje, ispisite elemente (paralelna iteracija)
# zip uparuje dvije liste prema indeksima
x = zip(brojevi, slova)

for idx, value in enumerate(x):
    print(value)





















