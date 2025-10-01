
# Conditional Tests

# 5.2

# Tests for equality and inequality with strings

car = 'toyota'
print(car == 'toyota')

car = 'ford'
print(car == 'toyota')

# Tests using the lower() method

car = 'Toyota'
print(car.lower() == 'toyota')

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

number = 9
print(number < 10)
print(number <= 11)
print(number >= 8)
print(number > 7)

# Tests using the and keyword and the or keyword

# and statement.

score_0 = 14
score_1 = 25
print(score_0 >= 18 and score_1 >= 25)

score_0 = 18
print(score_0 >= 18 and score_1 >= 25)

# or statement.

score_0 = 14
score_1 = 25
print(score_0 >= 18 or score_1 >= 25)

score_1 = 17
print(score_0 >= 18 or score_1 >= 25)

# Test whether an item is in a list

fruits = ['grapes', 'apple', 'mango']
print('grapes' in fruits)

# Test whether an item is not in a list

fruits = ['grapes', 'apple', 'mango']
print('banana' in fruits)