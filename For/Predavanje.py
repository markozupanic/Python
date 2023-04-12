fruits=["apple","orange","pineapple","banana"]
#for
for index in range(len(fruits)):
    if fruits[index]=="pineapple":
        continue
        #break
    print(fruits[index])
  
print("")
  
#obrnuto                    start,stop,step
for index in range(len(fruits) -1,-1,-1):
    if fruits[index]=="pineapple":
        continue
        #break
    print(fruits[index])    

print("")   

#for each
#for fruit in fruits:
#    print(fruit)





