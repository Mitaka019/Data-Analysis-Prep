
# 5.1 Introduction to pandas Data Structures

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Index Objects

obj = pd.Series(range(3), index = ['a', 'b', 'c'])
index = obj.index
print(index)

print(index[1:])

# index[1] = 'd' # TypeError

labels = pd.Index(np.arange(3))
print(labels)

obj2 = pd.Series([1.5, -2.5, 0], index = labels)
print(obj2)

print(obj2.index is labels)

# In addition to being array-like, an Index also behaves like a fixed-size set:

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
print(frame3)

print(frame3.columns)

print('Ohio' in frame3.columns)
print(2003 in frame3.index)

# Unlike Python sets, a pandas Index can contain duplicate labels:

dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])

print(dup_labels)

# Pandas Index Methods

# append        - Concatenate with additional Index objects, producing a new Index
# difference    - Compute set difference as an Index
# intersection  - Compute set intersection
# union         - Compute set union
# isin          - Compute boolean array indicating whether each value is contained in the passed collection
# delete        - Compute new Index with element at index i deleted
# drop          - Compute new Index by deleting passed values
# insert        - Compute new Index by inserting element at index i
# is_monotonic  - Returns True if each element is greater than or equal to the previous element
# is_unique     - Returns True if the Index has no duplicate values
# unique        - Compute the array of unique values in the Index
