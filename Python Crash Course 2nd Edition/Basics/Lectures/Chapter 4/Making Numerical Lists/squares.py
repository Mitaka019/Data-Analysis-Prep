
# Making Numerical Lists

# Using range() to Make a List of Numbers

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# To make it much simpler.

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions

# A list comprehension allows you to generate this same list in just one line of code.

squares = [value * 2 for value in range(1, 11)]
print(squares)

