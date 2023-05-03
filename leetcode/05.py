#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
x = 121
x_str=str(x)
x_lista=list(x_str)
x_obrnuto=x_lista[::-1]
x_zavrsno=""
for i in x_obrnuto:
    x_zavrsno+=str(i)  
if(x_str==x_zavrsno):
    print("True")
else:
    print("False")
