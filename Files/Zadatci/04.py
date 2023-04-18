#5. napisi program koji ce napraviti novu datoteku te pohraniti 
# u nju N nasumicno generiranih linija teksta u rasponu od 1-20 
# (preporuka: koristiti string i random library)
import random
import string
FILE_PATH="brojevi.txt"

def kreiraj_datoteku():
    f=open(FILE_PATH,"a")
    a=random.randint(1,20)
    i=0
    while i<a:
         letters = string.ascii_lowercase
         result_str = ''.join(random.choice(letters) for i in range(a))
         f.write(result_str)
         f.write("\n")
         i+=1
    f.close()
        
        





kreiraj_datoteku()





























