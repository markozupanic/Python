#16. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste

list_str_int=[1,"bjfd",6,"uvfdkb","jdbvjk"]
list_brojevi=[]
list_str=[]

counter=0
mjesto_u_listi=0

while counter<len(list_str_int):
    if(type(list_str_int[mjesto_u_listi])==int):
        list_brojevi.append(list_str_int[mjesto_u_listi])
    else:
        list_str.append(list_str_int[mjesto_u_listi])
    counter+=1
    mjesto_u_listi+=1

print(list_brojevi)
print(list_str)
    







