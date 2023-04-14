#1. napravite dva prazna rjecnika dictionary1 i dictionary2 (na oba nacina) i jedan rjecnik popunjen proizvoljnim parovima (min. 3).
# iz treceg rjecnika napravite sljedece:

dict_1={}
dict_2={}
dict_3={"name": "daniel", "age": 30,"country":"croatia","city":"osijek"}

#    a) ispisite sve kljuceve
keys=dict_3.keys()
print(keys)
#    b) ispisite sve vrijednosti
values=dict_3.values()
print(values)
#    c) ispisite vrijednost nekog kljuca
print(f"zovem se {dict_3.get('name')} zupanic")
#    d) ispisite tuple svih kljuceva u rjecniku
print(tuple(dict_3.keys()))