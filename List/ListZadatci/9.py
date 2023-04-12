#9. Napisi program koji ce ucitanu listu brojeva brojevi sortirati od najvece do
#najmanje vrijednosti i obrnuto.


num_list=[]

while(len(num_list)!=6):
    
    input_num=int(input("Input number: "))
    num_list.insert(0,input_num)
    

num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)







