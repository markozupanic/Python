#Kopirajte Numpy polje iz prethodnog zadatka, te novom polju promijenite tip u np.int16, te
#ispišite novi tip polja.

import numpy as np

a=np.random.rand(3,4,2).astype(np.int16)
print(f"Tip podatka: {a.dtype}")







