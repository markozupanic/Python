#13. zadan je rjecnik {'data1':100,'data2':-54,'data3':247}. napisi program koji mnozi sve vrijednosti u njemu.

data={'data1':100,'data2':-54,'data3':247}
data_list=list(data)
umnozak=1

for i in data:
    data[i]=int(data[i])
    umnozak*=data[i]
    print(umnozak)






