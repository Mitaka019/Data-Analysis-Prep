
# Using a while Loop with Lists and Dictionaries

# Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', 'glodfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)