#8. iscitaj datoteku iz prethodnog zadatka te ispisi broj ponavljanja svakog imena.
# prepravi sadrzaj datoteke tako da ispis bude sljedeceg formata:
#| broj_ponavljanja | ime
#| 1 | daniel |
#| 3 | mario |
from collections import Counter
FILE_PATH="pohranjivanje.txt"

def prebrojavanje_istih():
    f=open(FILE_PATH,"r")
    #print(f.readlines())
    a=f.readlines()
    b=a
    print(b)
    c = Counter(b)
    print(c)
    f.close()
    
    
prebrojavanje_istih()











