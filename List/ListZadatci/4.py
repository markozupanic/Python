#4. Deklarirajte list. Omogućite unos elemenata preko
#tipkovnice. Ispišite elemente niza.


list=[]
list_starting=0


while(True):
  list_input=input("Input: ")

  list.insert(list_starting,list_input)
  #print(list)
  
  if list_input=="0":
      break
  
print(list)








