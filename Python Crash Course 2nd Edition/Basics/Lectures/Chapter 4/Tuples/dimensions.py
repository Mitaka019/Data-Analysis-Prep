
# Tuples

# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

# Defining a Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

    
