#23. NapiÅ¡i program koji unosi jedan broj i ispisuje koji je broj djeljiv s tri najbliÅ¾i tom broju.


broj=int(input("Unesi broj: "))

if(broj%3==2):
    print(broj-2)
elif(broj%3==1):
    print(broj-1)
else:
    print(broj)


