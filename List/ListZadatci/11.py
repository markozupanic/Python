#11. Napisi program koji upisuje rezultat pet najboljih natjecatelja i ispisi koji rezultat je imao
#najbolji natjecatelj te koji je poredu on igrao.

number=[]



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

max_number=max(number)

if(max_number==number_input1):
    print(f"{max_number} and he played 1")
elif(max_number==number_input2):
    print(f"{max_number} and he played  2")
elif(max_number==number_input3):
    print(f"{max_number} and he played  3")
elif(max_number==number_input4):
    print(f"{max_number} and he played  4")
elif(max_number==number_input5):
    print(f"{max_number} and he played  5")













