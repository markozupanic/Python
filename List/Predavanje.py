

name1 = "daniel"
name2 = "antonio"
name3 = 2323424

names_list = [name1, name2, name3, True, 123.45]
print(names_list)
# dodajemo LISTU ["mario", "ivan"] na kraj names_list
names_list.append(["mario", "ivan"])
# ubacujemo "david" na 2. index, a ostale podatke pomicemo prema kraju
names_list.insert(2, "david")
print(names_list)
# prosirujemo postojecu listu names_list listom ["mario", "ivan"]
names_list.extend(["mario", "ivan"])
print(names_list)
# brisanje svih elemenata iz liste
names_list.clear()
names_list = []
# pop uklanja element iz liste; default: posljednji element
names_list.pop()
print(names_list)
# uklanjamo PRVI element iz liste
names_list.pop(0)
print(names_list)
abc_list = ["b", "c", "a", "c", "a", "c", "c"]
print(abc_list)
# sortiranje liste uzlazno/silazno
abc_list.sort(reverse=False)
print(abc_list)
# dohvaca poziciju PRVOG trazenog elementa
print(abc_list.index("c"))
# prebrojava trazene elemente
print(abc_list.count("c"))



# names_list[2] = "david"
# print(names_list[-1])

# print(names_list)
# print(names_list[:])








