#12. zbroji sve vrijednosti unutar rjecnika {"1": 1, "2": 2, "3": 3, "4": 4}

rjecnik={"1": 1, "2": 2, "3": 3, "4": 4}

rjecnik_list=list(rjecnik)
print(rjecnik_list)
zbroj=0
for i in range(len(rjecnik_list)):
    rjecnik_list[i]=int(rjecnik_list[i])
    zbroj+=rjecnik_list[i]
    print(zbroj)
    









