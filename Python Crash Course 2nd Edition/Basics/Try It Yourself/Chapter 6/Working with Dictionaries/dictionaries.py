
# Working with Dictionaries

# 6.1

person = {'first_name': 'rachel joy', 'last_name': 'matudio', 'age': 22, 'city': 'quezon city'}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

# 6.2

favorite_numbers = {
    "SpongeBob": 7,
    "Mickey Mouse": 3,
    "Bugs Bunny": 5,
    "Doraemon": 9,
    "Jerry": 2
}

print(f"\nSpongeBob's favorite number is {favorite_numbers['SpongeBob']}.")
print(f"Mickey Mouse's favorite number is {favorite_numbers['Mickey Mouse']}.")
print(f"Bugs Bunny's favorite number is {favorite_numbers['Bugs Bunny']}.")
print(f"Doraemon's favorite number is {favorite_numbers['Doraemon']}.")
print(f"Jerry's favorite number is {favorite_numbers['Jerry']}.")

# 6.3

glossary = {
    'Indentation': 'Indentation refers to the spaces at the beginning of a code line',
    'Comments': 'Comments are code lines that will not be executed',
    'Camel Case': 'Camel Case Variable Names',
    'Numbers': 'There are three numeric types in Python',
    'Operators': 'Use operator to perform operations in Python'
}

print(f"\nIndentation: {glossary['Indentation']}")
print(f"\nComments: {glossary['Comments']}")
print(f"\nCamel Case: {glossary['Camel Case']}")
print(f"\nNumbers: {glossary['Numbers']}")
print(f"\nOperators: {glossary['Operators']}")