#10. Napisi program koji unosi bodove pet najboljih natjecatelja te ispisuje
#koliko je bodova imao drugi najbolji natjecatelj.


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

number.sort()
print(f"Secon best:{number[3]}")











