#class Solution(object):
#    def isPalindrome(self, x):
x = 12
x_str=str(x)
x_lista=list(x_str)
x_obrnuto=x_lista[::-1]
x_zavrsno=""
print(x_zavrsno)
for i in x_obrnuto:
    print(i)
    x_zavrsno+=str(i)
     
if(x==x_zavrsno):
    True
    print("True")
else:
    False
    print("False")