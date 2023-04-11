# Napravi program za dijeljenje dva broja bez korištenja operatora za dijeljenje (/ , // ili %)


num1=int(input("input the number 1 : "))
num2=int(input("input the number 2 : ")) 
result=0;
div=num1+num2;
while(div>num2):
        div=div-num2;
        result=result+1
print("The division is",result)








