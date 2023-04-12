#12. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
#obrisanim duplikatima.



str_list=["marko","ankica","goran","ankica"]
count=0
while count<len(str_list):
  count_same=str_list.remove("ankica")
  count+=1

print(str_list)
















