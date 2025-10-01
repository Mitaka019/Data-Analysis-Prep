
# 4.3 Array-Oriented Programming with Arrays

import numpy as np

# The numpy.where function is a vectorized version of the ternary expression x if condition else y.

# Expressing Conditional Logic as Array Operations

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

results = [x if c else y for x, y, c in zip(xarr, yarr, cond)]
print(results)

result = np.where(cond, xarr, yarr)
print(result)

# A typical use of where in data analysis is to produce a new array
# of values based on another array.

arr = np.random.randn(4, 4)
print(arr)

print(arr > 0)

print(np.where(arr > 0, 2, -2))

print(np.where(arr > 0, 2, arr)) # Set only positive values to 2

# Mathematical and Statistical Methods

arr = np.random.randn(5, 4)
print(arr)

print(arr.mean())

print(np.mean(arr))

print(arr.sum())

print(arr.mean(axis=1))

print(arr.sum(axis=0))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())

# Other methods like cumsum and cumprod do not aggregate, instead producing an array
# of the intermediate results:

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)

print(arr.cumsum(axis = 0))
print(arr.cumprod(axis = 1))

# ===============================
# 🔹 Aggregation Functions (reduce values across an array or axis)
# ===============================
# sum        -> Sum of all elements in the array or along an axis
#               (zero-length arrays have sum = 0)

# mean       -> Arithmetic mean
#               (zero-length arrays have mean = NaN)

# std, var   -> Standard deviation and variance
#               (optional degrees of freedom adjustment, default denominator = n)

# min, max   -> Minimum and maximum element values

# argmin,
# argmax     -> Indices of the minimum and maximum elements

# cumsum     -> Cumulative sum of elements (starts from 0)

# cumprod    -> Cumulative product of elements (starts from 1)

# Methods for Boolean Arrays

arr = np.random.randn(100)
print((arr > 0).sum()) # Number of positive values

bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

# Sorting

arr = np.random.randn(6)
print(arr)

print(arr.sort())

print(arr)

arr = np.random.randn(5, 3)
print(arr)

print(arr.sort(1))
print(arr)

large_arr = np.random.randn(1000)
print(large_arr.sort())
print(large_arr[int(0.05 * len(large_arr))]) # 5% quantile

# Unique and Other Set Logic

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

print(np.unique(ints))

print(sorted(set(names)))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.isin(values, [2, 3, 6]))

# ===============================
# 🔹 Set Logic Functions (array set operations)
# ===============================

# unique(x)         -> Compute the sorted, unique elements in x

# intersect1d(x, y) -> Compute the sorted, common elements in x and y

# union1d(x, y)     -> Compute the sorted union of elements from both arrays

# in1d(x, y)        -> Return a boolean array indicating whether each element of x is in y

# setdiff1d(x, y)   -> Set difference: elements in x that are not in y

# setxor1d(x, y)    -> Symmetric difference:
#                      elements that are in either of the arrays, but not both

