
# 5.1 Introduction to pandas Data Structures

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# DataFrame

# A DataFrame represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type (numeric, string,
# boolean, etc.).

# There are many ways to construct a DataFrame, though one of the most common is
# from a dict of equal-length lists or NumPy arrays:

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

print(frame)

# For large DataFrames, the head method selects only the first five rows:

print(frame.head())

# If you specify a sequence of columns, the DataFrame’s columns will be arranged in
# that order:

print(pd.DataFrame(data, columns = ['year', 'state', 'pop']))

# If you pass a column that isn’t contained in the dict, it will appear with missing values
# in the result:

frame2 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'],
                      index = ['one', 'two', 'three', 'four', 'five', 'six'])

print(frame2)

print(frame2.columns)

# A column in a DataFrame can be retrieved as a Series either by dict-like notation or
# by attribute:

print(frame2['state'])

print(frame2.year)

# frame2[column] works for any column name, but frame2.column
# only works when the column name is a valid Python variable
# name.

# Rows can also be retrieved by position or name with the special loc attribute (much
# more on this later):


print(frame2.loc['three'])

frame2['debt'] = 16.5
print(frame2)

frame2['debt'] = np.arange(6.)
print(frame2)

# When you are assigning lists or arrays to a column, the value’s length must match the
# length of the DataFrame. If you assign a Series, its labels will be realigned exactly to
# the DataFrame’s index, inserting missing values in any holes:

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2['debt'] = val
print(frame2)

# Assigning a column that doesn’t exist will create a new column. The del keyword will
# delete columns as with a dict.

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

del frame2['eastern']
print(frame2.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
print(frame3)

# You can transpose the DataFrame (swap rows and columns) with similar syntax to a
# NumPy array:

print(frame3.T)

# The keys in the inner dicts are combined and sorted to form the index in the result.
# This isn’t true if an explicit index is specified:

print(pd.DataFrame(pop, index = [2001, 2002, 2003]))

# Dicts of Series are treated in much the same way:

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}

print(pd.DataFrame(pdata))

# If a DataFrame’s index and columns have their name attributes set, these will also be
# displayed:

frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)

# As with Series, the values attribute returns the data contained in the DataFrame as a
# two-dimensional ndarray:

print(frame3.values)

# If the DataFrame’s columns are different dtypes, the dtype of the values array will be
# chosen to accommodate all of the columns:

print(frame2.values)

# Pandas DataFrame Input Types

# 2D ndarray                - A matrix of data, optional row and column labels can be passed
# dict of arrays/lists/tuples- Each sequence becomes a column; all must be the same length
# NumPy structured/record array - Treated like "dict of arrays"
# dict of Series             - Each value becomes a column; indexes are unioned to form the row index if none is passed
# dict of dicts              - Each inner dict becomes a column; keys are unioned to form the row index (like dict of Series)
# list of dicts or Series    - Each item becomes a row; union of keys/indexes become column labels
# list of lists or tuples    - Treated like "2D ndarray"
# another DataFrame          - Uses the DataFrame’s indexes unless different ones are passed
# NumPy MaskedArray          - Like "2D ndarray", except masked values become NA/missing
