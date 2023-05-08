#Stvorite 2D ndarray dimenzija 5x6 nasumičnih vrijednosti. Bez korištelja for petlje izdvojite svaki
#drugi stupac u zasebnu varijablu. Također, u zasebnu varijablu izdvojite posljednja 3 retka
import numpy as np
a=np.random.rand(5,6)
#print(a[0:3:2,1::2])#red ,stup

svaki_drugi_stupac=a[::,0::2]
posljednja_tri_retka=a[:3:1,::]

print(svaki_drugi_stupac)
print("")
print(posljednja_tri_retka)



















