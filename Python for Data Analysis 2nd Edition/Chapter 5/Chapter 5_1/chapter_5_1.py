
# 5.1 Introduction to pandas Data Structures

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series

# A Series is a one-dimensional array-like object containing a sequence of values (of
# similar types to NumPy types) and an associated array of data labels, called its index.

obj = pd.Series([4, 7, -5, 3])
print(obj)

print(obj.values)
print(obj.index) # like range(4)

# Often it will be desirable to create a Series with an index identifying each data point
# with a label:

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)

print(obj2.index)

# Compared with NumPy arrays, you can use labels in the index when selecting single
# values or a set of values:


print(obj2['a'])

obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

print(obj2[obj2 > 0])

print(obj2 * 2)

print(np.exp(obj2))

# Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. It can be used in many contexts where you might
# use a dict:

print('b' in obj2)
print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)
print(obj3)

# You can override this by passing the dict keys in the order you
# want them to appear in the resulting Series:

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index = states)
print(obj4)

# Here, three values found in sdata were placed in the appropriate locations, but since
# no value for 'California' was found, it appears as NaN (not a number), which is con‐
# sidered in pandas to mark missing or NA values. Since 'Utah' was not included in
# states, it is excluded from the resulting object.

print(pd.isnull(obj4))

print(pd.notnull(obj4))

print(obj4.isnull())

# A useful Series feature for many applications is that it automatically aligns by index
# label in arithmetic operations:

print(obj3)
print(obj4)
print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# A Series’s index can be altered in-place by assignment:

print(obj)

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

