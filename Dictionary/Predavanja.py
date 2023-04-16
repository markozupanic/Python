import random
# kreira dict
personal_data = {"name": "daniel", "age": 30}
# azurira vrijednost na kljucu; kreira novi ako ne postoji
personal_data.update({"gender": "M"})
personal_data.update({"alias": ["dani", "dano"]})
# ispisuje listu kljuceva
keys = personal_data.keys()
print(keys)
print(f"zovem se {personal_data['name']}")
print(f"imam {personal_data.get('age')} godina")
print(f"moj nadimak je {random.choice(personal_data.get('alias'))}")
# ispis kljuceva preko petlje
for key in keys:
    print(key)

d1 = {"name": "dani"}
d2 = d1.copy()
d1.update({"age": 30})
print(d1)
# dohvacanje preko kljuca
print(d2.get("age"))
print(d2)
# dohvaca kljuc ako postoji; u protivnom "inserta" novi kljuc
print(d2.setdefault("age"))
print(d2)
d2.update({"age": 30})
print(d2)
d2.pop("age")
print(d2)
personal_data = {"name": "daniel", "age": 30}
print(personal_data.keys())
print(personal_data.values())
print(personal_data.items())

# primjeri sa petljama
for key in personal_data.keys():
    print(key, end=" ")
print()
for value in personal_data.values():
    print(value, end=" ")
print()
for key, value in personal_data.items():
    print(f"kljuc {key} ima vrijednost {value}")

my_keys = ["model", "type", "year", "power"]
d3 = {}
# postavlja predefiniranu listu kljuceva na nekakvu dogovorenu vrijednost
d3 = d3.fromkeys(my_keys, 0)
print(d3)
d4 = {2.3: "asd"}
print(d4.get(2.3))


