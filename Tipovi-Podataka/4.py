broj=int(input("Unesi broj: "))

x=broj//100
print(x)
x1=(broj-x*100)//10
print(x1)
x2=(broj-x*100-x1*10)
print(x2)
print(x+x1+x2)