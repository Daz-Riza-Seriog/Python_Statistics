###############################################################################################################
#                                   Numpy Array                                                               #
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. #
# The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the  #
# size of the array along each dimension.                                                                     #
###############################################################################################################

import numpy as np

### Create a 3x1 numpy array
a = np.array([1,2,3])
print('\nArray 3*1:\t',a)

### Print object type
print('\nClass of the Array:\t',type(a))

### Print shape
print('\nShape of the Array:\t',a.shape)

### Print some values in a
print('\nValues of [0],[1],[2]:\t',a[0], a[1], a[2])

### Create a 2x2 numpy array
b = np.array([[1,2],[3,4]])
print('\nArray of 2*2:\n',b)

### Print shape
print('\nShape of the Array:\t',b.shape)

## Print some values in b
print('\nValues of b:\t',b[0,0], b[0,1], b[1,1])

### Create a 3x2 numpy array
c = np.array([[1,2],[3,4],[5,6]])
print('\nArray of 3*2:\n',c)

### Print shape
print('\nShape of the Array:\t',c.shape)

### Print some values in c
print('\nValues of c:\t',c[0,1], c[1,0], c[2,0], c[2,1])

### 2x3 zero array
d = np.zeros((2,3))
print('\nZero Array 2*3:\n',d)

### 4x2 array of ones
e = np.ones((4,2))
print('\nArray of Ones 4*2:\n',e)

### 2x2 constant array
f = np.full((2,2), 9)
print('\nArray of Constant 9:\n',f)

### 3x3 random array
g = np.random.random((3,3))
print('\nRandom Array 3*3:\n',g)

################################################
#              Array Indexing                  #
################################################\

### Create 3x4 array
h = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])
print('\nArray 3*4:\n',h)

### Slice array to make a 2x2 sub-array
i = h[:2, 1:3]
print('\nSlice Array to make sub Array:\n',i)


################################################
#              Datatypes in Arrays             #
################################################

### Integer
j = np.array([1, 2])
print('\nFuction type:\t',j.dtype)

### Float
k = np.array([1.0, 2.0])
print('\nType:\t',k.dtype)

### Force Data Type
l = np.array([1.0, 2.0], dtype=np.int64)
print('\nForce Change in DataType:\t',l.dtype)

#########################################################################
#                           Array Math                                  #
#   Basic mathematical functions operate elementwise on arrays,         #
#   and are available both as operator overloads and as functions       #
#   in the numpy module:                                                #
#########################################################################

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print('\nSum Array classical `+`:\n',x + y)
print('\nSum Array `np.add(x,y)` :\n',np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print('\nRest Array classical `-`:\n',x - y)
print('\nRest Array `np.subtract(x,y)` :\n',np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print('\nProduct Array classical `*`:\n',x * y)
print('\nProduct Array `np.multiply(x,y)` :\n',np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print('\nDivision Array classical `/`:\n',x / y)
print('\nDivision Array `np.divide(x,y)` :\n',np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print('\nsquare Root Array `np.sqrt(x)` :\n',np.sqrt(x))


x = np.array([[1,2],[3,4]])

### Compute sum of all elements; prints "10"
print('\nSum of all elements Array `np.sum(x)`\n',np.sum(x))

### Compute sum of each column; prints "[4 6]"
print('\nSum of ech column Array `np.sum(x, axis=0)`\n',np.sum(x, axis=0))

### Compute sum of each row; prints "[3 7]"
print('\nSum of ech row Array `np.sum(x, axis=1)`\n',np.sum(x, axis=1))

### Compute mean of all elements; prints "2.5"
print('\nMean of all elements in Array `np.mean(x)`\n',np.mean(x))

### Compute mean of each column; prints "[2 3]"
print('\nMen  of ech Column in Array `np.mean(x, axis=1)`\n',np.mean(x, axis=0))

### Compute mean of each row; prints "[1.5 3.5]"
print('\nMean of each Row elements in Array `np.mean(x, axis=1)`\n',np.mean(x, axis=1))