#7. Napisi program koji unosi pet ocjena te ih sprema u listu, a zatim racuna i ispisuje njihov
#prosjek.


number=[]
#sum_numbers=0

number_input1=int(input("Input number: "))
number_input2=int(input("Input number: "))
number_input3=int(input("Input number: "))
number_input4=int(input("Input number: "))
number_input5=int(input("Input number: "))
number.insert(0,number_input1)
number.insert(0,number_input2)
number.insert(0,number_input3)
number.insert(0,number_input4)
number.insert(0,number_input5)
print(number)

number_sum=sum(number)
print(number_sum/5)











