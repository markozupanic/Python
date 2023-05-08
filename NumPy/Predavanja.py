import numpy as np

python_1d_polje=[[1,2,3],[4,5,6]]
numpy_polje=np.array(python_1d_polje,dtype=np.int16)

print("Broj osi:{}".format(numpy_polje.ndim))
print("Dimenzije polja:{}".format(numpy_polje.shape))
print("Broj elemenata u polju:{}".format(numpy_polje.size))
print("Tip elemenata:{}".format(numpy_polje.dtype))

np_zeros=np.zeros((2,3))
print(np_zeros)
print("")
np_ones=np.ones((2,3))
print(np_ones)
print("")
np_empty=np.empty((2,3))
print(np_empty)
print("")
np_full=np.full((2,3),13)
print(np_full)
print("")
np_eye=np.eye(5)
print(np_eye)
print("")
a=np.arange(2,10,2)
print(a)
print("")
b=np.linspace(5,10,num=5)
print(b)
print("")
c=np.random.randint(10,100,10)
print(c)
print("")
d=np.array([1,2,3])
e=np.array([4,5,6])
f=np.matmul(d,e)
print(f)

g=np.array([1,2,3,4,5,6])
print(g[4])
g[2]=7
print(g)

h=np.array([1,2,3,4,5,6])
h[:4]=0
print(h)
