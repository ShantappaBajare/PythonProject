""" Creation of numpy arrays """
# import numpy as np
# a = np.array([1,2,3,4,5])
# print(a)

"""
1. array()
2. arange()
3. linspace()
4. full()()
5. zeros()
6. ones()
7. eye()
8. identity()
9. empty()
10. random library functions
    1. randint()
    2. random.uniform()
    3. random.normal()
    4. random.rand()
    5. random.randn()
    6. random.shuffle()
    
Array attributes:
----------------------------
1. shape -shape of array
2. size - to get size of array
3. itemsize- the size of each array element in bytes
4. ndim- to get dimension
5. dtype- to get data type

Numpy Data types:
===============================
i-int
b-bool
c-complex
u-unsigned
U-unicode string
f-float
m-date
s-string

array slicing:
arrayname[start:end:step]


"""

import numpy as np
# a = np.array([1,2,3,4,5])
#
# print(a.shape) # (5,)-tuple
# print(a.size)  # 5 - int
# print(a.itemsize) # 8-int
# print(a.ndim) # 1 int
# print(a.dtype) # int64

# b = np.array([[1,2,3],[6,7,8]])
#
# print(b.shape) # (2,3)-tuple
# print(a.size)  # 6 - int
# print(a.itemsize) #
# print(a.ndim) # 1 int
# print(a.dtype) # int64

"""
Accessing nd array elements using
1. indexing- ordered arrary
2. slicing- ordered
3. Advanced indexing-orbitary elements- it will accept nd array or list as argument
"""

"""accessing 1D orbitary array elements"""

# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a)
#
# # access 1,3,7 from the array
# # way-1 create nd array with required indexes and passing that array as argument
#
# indexes= np.array([0,2,6])
# print(a[indexes]) #[1 3 7]
#
# # way-2 create list required indexes and pass it to the array as arguments
#
# l=[0,2,6]
# print(a[l])
# print(a[(0,2,6)])#IndexError: too many indices for array: array is 1-dimensional,
                 # but 3 were indexed tuples not alloed

"""accessing 2d array"""

#syntax= [(row_indexes),(column_indexes)]