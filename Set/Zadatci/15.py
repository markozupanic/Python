#16. napisi funkciju koja prima dva skupa razlicitih duljina A i B. ako je neki od ta dva skupa podskup drugome,
# ispisi razliku tih dvaju skupova (od nadskupa oduzmi podskup); ako nisu, napravi uniju i presjek skupova.


a={2,4,5,7,41,5,3,5,41,9,8,2,3}
b={453,7864153,4153,513}

if(a&b==b):
    print(a-b)
elif(b&a==a):
    print(b-a)
else:
    print(a|b)
    print(a&b)










