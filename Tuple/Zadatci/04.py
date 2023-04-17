#5. iz tuple-a iz prethodnog zadatka napravite sljedece:
#    a) ispisite prvi element
#    b) ispisite posljednji element
#    c) pomocu slicing operatora ':', ispisite sve elemente osim prva dva i posljednja 2
#    d) koristeci for petlju, ispisite tuple
#    e) ispisite duljinu tuple-a

tuple_brojevi=(10, 20, 30, 40, 50, 60, 70, 80, 90)

#    a) ispisite prvi element
print(tuple_brojevi[0])
#    b) ispisite posljednji element
print(tuple_brojevi[-1])
#    c) pomocu slicing operatora ':', ispisite sve elemente osim prva dva i posljednja 2
print(tuple_brojevi[2:-2])
#    d) koristeci for petlju, ispisite tuple
for i in tuple_brojevi:
    print(i)
#    e) ispisite duljinu tuple-a
print(len(tuple_brojevi))










