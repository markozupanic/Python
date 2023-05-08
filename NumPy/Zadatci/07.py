#Stvorite jediničnu matricu dimenzije 4x4, te još jednu matricu istih dimenzija čiji svi elementi
#imaju vrijednost 9. Ispišite na ekran:
import numpy as np
a=np.ones((4,4))
b=np.full((4,4),9)
#● Zbroj
print(a+b)
#● Razliku
print(a-b)
#● Umnožak (element po element)
print(a*b)
#● Količnik
print(a/b)