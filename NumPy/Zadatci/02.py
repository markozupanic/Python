#Stvorite Numpy array objekt nasumičnih brojeva veličine 3x4x2. Za generiranje nasumičnih
#brojeva koristite odgovarajuću Numpy funkciju. Tip elemenata Numpy polja mora biti
#numpy.float64.
#Ispišite na ekran:

import numpy as np 
a=np.random.rand(3,4,2).astype(np.float64)

print(a)
print(a.dtype)
#● Broj osi
print(f"Broj osi:{a.ndim}")
#● Dimenzije polja
print(f"Dimenzije polja:{a.shape}")
#● Ukupni broj elemenata u polju
print(f"Ukipni broj elemenata: {a.size}")
#● Tip elemenata u polju
print(f"Tip elemenata u polju: {a.dtype}")