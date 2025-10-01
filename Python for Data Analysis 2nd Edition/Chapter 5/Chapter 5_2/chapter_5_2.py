
# 5.2 Essential Functionality

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Reindexing

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

# Calling reindex on this Series rearranges the data according to the new index, introducing missing values if any index values were not already present:

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# The method option allows us to do this, using a method such as ffill, which forward-fills the values:

obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
print(obj3)

print(obj3.reindex(range(6), method ='ffill'))

# With DataFrame, reindex can alter either the (row) index, columns, or both. When
# passed only a sequence, it reindexes the rows in the result:

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), 
                     index = ['a', 'c', 'd'],
                     columns = ['Ohio', 'Texas', 'California'])

print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

# The columns can be reindexed with the columns keyword:

states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))

# As we’ll explore in more detail, you can reindex more succinctly by label-indexing
# with loc, and many users prefer to use it exclusively:

# Pandas Reindexing Parameters
#
# index      : New sequence to use as index (Index or sequence-like). 
#              If Index, it is used as-is without copying.
# method     : Interpolation method for filling values. 
#              'ffill' → forward fill, 'bfill' → backward fill.
# fill_value : Value to use when introducing missing data.
# limit      : Max number of elements to fill when using forward/backward fill.
# tolerance  : Max numeric distance to fill for inexact matches (when ffill/bfill).
# level      : For MultiIndex, match on specific level; otherwise subset selection.
# copy       : If True, always copy data even if indexes are equivalent. 
#              If False, no copy when indexes are the same.

# Dropping Entries from an Axis

