# inicijalizacija seta
set_example = {}
# inicijalizacija sa podacima
my_set = {4, 5, 1, 2, 3, 3, 3, 3, "da", "da"}
print(my_set)
# pop izbacuje "random" element iz seta
a = my_set.pop()
print(my_set)
print(a)
# add radi slicno kao i append kod liste, dodaje element
my_set.add(3)
print(my_set)
my_set.add(5454)
print(my_set)

my_list = [5, 2, 1, 7, 8]
# pretvorba liste u set
new_set = set(my_list)
# pretvorba seta u listu
my_unique_list = list(new_set)
print(my_list)
print(new_set)

a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 8}
# operacije
print(f"unija: {a | b}")
print(f"presjek: {a & b}")
print(f"a \ b: {a - b}")
print(f"b \ a: {b - a}")
print(f"a ^ b: {a ^ b}")

my_list = ["dani", "iva", "dani", "dani"]
print(my_list)
my_set = set(my_list)
print(my_set)
if "dani" in my_set:
    print("yes")
my_names = list(my_set)
print(my_names)
