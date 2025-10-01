
# 4.1 The NumPy ndarray: A Multidimensional Array Object

import numpy as np

# Generate some random data

data = np.random.randn(2, 3)
print(data)

print(data * 10)

print(data + data)

print(data.shape)
print(data.dtype)

# Creating ndarrays

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print(arr1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

print(arr2)

# Nested sequences, like a list of equal-length lists, will be converted into a multidimensional array

print(arr2.ndim)
print(arr2.shape)

print(arr1.dtype)
print(arr2.dtype)

print(np.zeros(10))

# To create a higher dimensional array with these methods, pass a tuple
# for the shape.

print(np.zeros((3, 6)))

print(np.empty((2, 3, 2)))

# arange is an array-valued version of the built-in Python range function:

print(np.arange(15))

# NumPy Array Creation Functions
#
# array        : Convert input data (list, tuple, array, or sequence) to an ndarray. 
#                Copies by default; dtype can be inferred or specified.
# asarray      : Convert input to ndarray, but avoid copying if already an ndarray.
# arange       : Like Python's range(), but returns an ndarray instead of a list.
#
# ones / ones_like   : Create an array of all 1s with given shape/dtype. 
#                      ones_like uses another array’s shape/dtype.
# zeros / zeros_like : Like ones/ones_like, but filled with 0s.
# empty / empty_like : Create arrays with uninitialized values. 
#                      Shape/dtype same as given or another array.
# full / full_like   : Create arrays filled with a specified value. 
#                      full_like uses another array’s shape/dtype.
#
# eye / identity     : Create an N × N identity matrix (1s on diagonal, 0s elsewhere).

# Data Types for ndarrays

# The data type or dtype is a special object containing the information (or metadata,
# data about data) the ndarray needs to interpret a chunk of memory as a particular
# type of data.

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr1 = np.array([1, 2, 3], dtype=np.int32)

print(arr1.dtype)
print(arr2.dtype)

# NumPy Data Types (dtypes)
#
# Integers:
# int8,  uint8   (i1, u1)  : Signed / Unsigned 8-bit (1 byte)
# int16, uint16  (i2, u2)  : Signed / Unsigned 16-bit
# int32, uint32  (i4, u4)  : Signed / Unsigned 32-bit
# int64, uint64  (i8, u8)  : Signed / Unsigned 64-bit
#
# Floating Point:
# float16  (f2)       : Half-precision float
# float32  (f4, f)    : Single-precision float (C float)
# float64  (f8, d)    : Double-precision float (C double, Python float)
# float128 (f16, g)   : Extended-precision float
#
# Complex Numbers:
# complex64   (c8)   : Two 32-bit floats (real + imaginary)
# complex128  (c16)  : Two 64-bit floats
# complex256  (c32)  : Two 128-bit floats
#
# Other Types:
# bool (?)         : Boolean (True/False)
# object (O)       : Generic Python object
# string_ (S)      : Fixed-length ASCII string (1 byte/char), e.g., 'S10'
# unicode_ (U)     : Fixed-length Unicode string, e.g., 'U10'

# You can explicitly convert or cast an array from one dtype to another using ndarray’s
# astype method:

arr = np.array([1, 2, 3, 4, 5,])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)

print(arr.astype(np.int32))

#numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.unicode_)

#print(numeric_strings.astype(float))

int_array = np.arange(10)

calibers = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float64)

print(int_array.astype(calibers.dtype))

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)