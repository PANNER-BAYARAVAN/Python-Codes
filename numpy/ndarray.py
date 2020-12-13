#The example below creates a Python list of 3
#floating point values, then creates an ndarray
#from the list and access the arrays’ shape and data type.

from numpy import array
l = [1.0, 2.0, 3.0]
a = array(l)
print(a)
print(a.shape)
print(a.dtype)
