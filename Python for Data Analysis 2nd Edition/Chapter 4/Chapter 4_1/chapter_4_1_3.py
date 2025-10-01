
# 4.1 The NumPy ndarray: A Multidimensional Array Object

import numpy as np

# Boolean Indexing

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data = np.random.randn(7, 4)

print(names)

print(data)

print(names == 'Bob')

print(data[names == 'Bob'])

# The boolean array must be of the same length as the array axis it’s indexing.

print(data[names == 'Bob', 2:])

print(data[names == 'Bob', 3])

# To select everything but 'Bob', you can either use != or negate the condition using ~:

print(names != 'Bob')

print(data[~(names == 'Bob')])

# The ~ operator can be useful when you want to invert a general condition:

cond = names == 'Bob'
print(data[~cond])

# Selecting two of the three names to combine multiple boolean conditions, use
# boolean arithmetic operators like & (and) and | (or):

mask = (names == 'Bob') | (names == 'Will')
print(mask)

print(data[mask])

# To set all of the negative values in data to 0 we need only do:

data[data < 0] = 0
print(data)

# Setting whole rows or columns using a one-dimensional boolean array is also easy:

data[names != 'Joe'] = 7
print(data)

# Fancy Indexing

# Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays.

arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])

print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
print(arr)

print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

# Here the elements (1, 0), (5, 3), (7, 1), and (2, 2) were selected. Regardless of
# how many dimensions the array has (here, only 2), the result of fancy indexing is
# always one-dimensional.

print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

# Transposing Arrays and Swapping Axes

arr = np.arange(15).reshape((3, 5))
print(arr)

print(arr.T)

arr = np.random.randn(6, 3)
print(arr)

print(np.dot(arr.T, arr))

# For higher dimensional arrays, transpose will accept a tuple of axis numbers to per‐
# mute the axes (for extra mind bending):

arr = np.arange(16).reshape((2, 2, 4))
print(arr)

print(arr.transpose((1, 0, 2)))

# Simple transposing with .T is a special case of swapping axes. ndarray has the method
# swapaxes, which takes a pair of axis numbers and switches the indicated axes to rear‐
# range the data:

print(arr)

print(arr.swapaxes(1, 2))