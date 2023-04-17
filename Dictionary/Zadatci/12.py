#15. napisi rjecnik sa proizvoljnim vrijednostima i neka sadrzi duplikate.
# napisi program koji bi uklonio sve parove koji sadrze duplikate.

rjecnik={'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
rjecnik_values=rjecnik.values()
rjecnik_list=list(rjecnik_values)
print(rjecnik_list)
rijec=0

for i in rjecnik_list:
    #print(i)
    if(i==rjecnik_list[rijec]):
        rjecnik_list.pop(i)
        rijec+=1
        
        
print(rjecnik_list)

















