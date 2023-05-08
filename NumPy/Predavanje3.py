from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
slika=Image.open("houses.jpg")
slika_numpy=np.asarray(slika)
print(type(slika))
print(type(slika_numpy))
print(slika_numpy.dtype)

slika_pil=Image.fromarray(slika_numpy)
print(type(slika_pil))
#slika_pil.save("moja_nova_slika.jpg")
print(slika_numpy.shape)

#plt.imshow(slika_numpy) prikaz slike
#plt.show()


#crveni_kanal=slika_numpy[:,:,0]
#plt.imshow(crveni_kanal,cmap='gray')
#plt.show()


slika_numpy = np.asarray(slika).copy() # create a writable copy of the array
slika_numpy[:,:,0] = 0
slika_numpy[:,:,1] = 0

plt.imshow(slika_numpy)
plt.show()

