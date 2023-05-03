#Input: x = 123
#Output: 321

x = 123
x_str=str(x)
x_lista=list(x_str)
x_obrnuto=x_lista[::-1]
x_zavrsno=""
for i in x_obrnuto:
    x_zavrsno+=str(i)
print(x_zavrsno)