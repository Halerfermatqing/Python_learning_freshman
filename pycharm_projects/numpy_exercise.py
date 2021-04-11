import numpy as np
a = np.array([1,2,3,4])
b = np.array([10,11,12,13])
print(a,b)
print(a.dtype,a.shape,a.ndim,)

c = np.array([[10,11,12],[20,21,22]])
print(c)
print(c.shape,c.ndim,c.dtype)

d = np.ones((3,4),dtype= int)
print(d)

d = np.empty((3,4),dtype= int)
print(d)

e = np.arange(9)
print(e)