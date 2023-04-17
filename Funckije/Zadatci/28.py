#28. napisi funkciju koja prima string i cijeli broj te ispisuje slova ciji su indeksi djeljivi sa predanim cijelim brojem 
# (npr. za unos "dananas", 2 => "dnns"; za unos "dananas", 1 => "dananas").


def djeljenje_stringa():
    unos_broja=int(input("Unesite broj za djeljenje: "))
    unos_stringa=input("Unesite rijec: ")
    counter=0
    
    while counter<len(unos_stringa):
      novi_string=unos_stringa[counter]
      print(novi_string)
      counter+=unos_broja
      
      
      
        


djeljenje_stringa()