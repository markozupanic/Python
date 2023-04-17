#2. iz tuple-a (10, 20, 30, 40, 50, 60) raspakiraj sve vrijednosti (bez koristenja *)
tuple_brojevi=(10, 20, 30, 40, 50, 60)
a,b,c,d,e,f=tuple_brojevi
print(a,b,c,d,e,f)

#3. iz prethodnog zadatka, koristenjem *, raspakiraj vrijednosti na sljedeci nacin:
#    a) spremi vrijednosti u 3 varijable (po zelji)
a,b,c,*ostali=tuple_brojevi
print(a,b,c)
print(ostali)
#    b) spremi vrijednosti u 2 varijable (po zelji)
a,b,*brojevi=tuple_brojevi
print(a,b)
print(brojevi)
#    c) spremi prvu i posljednju vrijednost u dvije varijable te vrijednosti izmedju njih u trecu
a,*other,d=tuple_brojevi

print(a,d)
print(other)
















