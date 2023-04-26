#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
l1 = [2,4,3]
l2 = [5,6,4]
prazni_prvi=""
prazni_drugi=""
for i in l1:
    #print(i)
    prazni_prvi+=str(i)
for i in l2:
    #print(i)
    prazni_drugi+=str(i)  
zbroj=int(prazni_prvi[::-1])+int(prazni_drugi[::-1])
print(zbroj)









