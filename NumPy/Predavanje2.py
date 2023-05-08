import numpy as np

#a=np.array([[1,2,3,4],
#           [5,6,7,8,],
#           [9,10,11,12],
#           [13,14,15,16]])

#print(a[0:3:2,1::2])#red ,stup



#b=np.random.randint(10,100,10)
#c=b.copy()
#c[0]=0
#print(b)
#print(c)






#d=np.random.randint(10,100,4)
#print(d)
#e=d.reshape((2,2,1))#u matrciu 2*2
#f=e.reshape((4,))#iz matrice u vektor
#print(e)
#print(f)


d=np.array([[1,2,3,4],
            [5,6,7,8]])
e=d.swapaxes(0,1)
print(e)

f=np.ones((3,4))
print(f.shape)
g=np.expand_dims(f,2)
print(g.shape)
g=g.squeeze()
print(g.shape)



h=np.array([[1,2],[3,4]])
i=np.array([[5,6]])
j=np.concatenate((h,i),axis=0)
print(j)


