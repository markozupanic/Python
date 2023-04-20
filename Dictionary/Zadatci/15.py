#18. zadan je rjecnik:
inventory = {'gold' : 500,
    'pouch' : ['flint', 'twine', 'tinder'],
    'backpack' : ['house key','dagger', 'bedroll','bread loaf']}
print(inventory)
# a) uklonite dagger iz backpack-a
inventory.pop("gold")
print(inventory)
# b) uvecajte gold za 50
inventory.setdefault("gold")
inventory.update({"gold":550})
print(inventory)
# c) uklonite flint i tinder iz pouch i dodajte flint&tinder
print(inventory.values())
inventori_vrijednosti=list(inventory.values())
invent_remove=inventori_vrijednosti[0]
invent_remove.remove('flint')
invent_remove.remove('tinder')
print(inventori_vrijednosti)
#invent_add=inventori_vrijednosti[0]
inventory.update({"pouch": "flint&tinder"})
print(inventory)






#list_inventori=list(inventory)
#print(list_inventori)
   
   
   
   
   
# d) kreirajte pocket te smjestite gold i house key u njega
   
   
   
   
   