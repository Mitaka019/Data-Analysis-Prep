
# Working with Part of a List

# 4.10

fruits = ['apple', 'grapes', 'oranges', 'lemon', 'mango']

print("The first three items in the list are:")
print(fruits[0:3])

print("\nThree items from the middle of the list are:")
print(fruits[1:4])

print("\nThe last three items in the list are:")
print(fruits[-3:])

# 4.11

my_pizzas = ['pepperoni', 'hawaiian', 'neopolitan']
friend_pizzas = my_pizzas[:]

my_pizzas.append('all meat')
friend_pizzas.append('extra cheese')

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(f"-{pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"-{pizza}")

# 4.12

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_pizzas:
    print(f"- {food}")