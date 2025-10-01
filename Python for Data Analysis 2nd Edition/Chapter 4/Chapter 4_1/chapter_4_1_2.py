
# 4.1 The NumPy ndarray: A Multidimensional Array Object

import numpy as np

# Arithmetic with NumPy Arrays

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)

print(arr * arr)

print(arr - arr)

print(1 / arr)

print(arr ** 0.5)

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)

print(arr2 > arr)

# Basic Indexing and Slicing

arr = np.arange(10)
print(arr)

print(arr[5])

print(arr[5:8])

arr[5:8] = 12
print(arr)

# As you can see, if you assign a scalar value to a slice, as in arr[5:8] = 12, the value is
# propagated (or broadcasted henceforth) to the entire selection.

arr_slice = arr[5:8]
print(arr_slice)

arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d[2])

# . But that is a bit too much work, so you can pass a comma-separated list of indices to select individual elements.
# So these are equivalent.

print(arr2d[0][2])

print(arr2d[0, 2])

# In multidimensional arrays, if you omit later indices, the returned object will be a
# lower dimensional ndarray consisting of all the data along the higher dimensions.

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3d)

print(arr3d[0])

old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)

arr3d[0] = old_values
print(arr3d)

print(arr3d[1, 0])

x = arr3d[1]
print(x)

print(x[0])

# Indexing with slices

print(arr)

print(arr[1:6])

print(arr2d)

print(arr2d[:2])

# When slicing like this, you always obtain array views of the same number of dimensions. By mixing integer indexes and slices, you get lower dimensional slices.

print(arr2d[1, :2])
print(arr2d[:2, 2])

print(arr2d[:, :1])

arr2d[:2, 1:] = 0
print(arr2d)