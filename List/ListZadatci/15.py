#15. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat

num_list=[5,6,4,3,2,7]

counter=0
poredak_lista=0

while counter<len(num_list):
    kvadrat_broja_u_listi=num_list[poredak_lista]**2
    
    poredak_lista+=1
    counter+=1

    print(kvadrat_broja_u_listi)







