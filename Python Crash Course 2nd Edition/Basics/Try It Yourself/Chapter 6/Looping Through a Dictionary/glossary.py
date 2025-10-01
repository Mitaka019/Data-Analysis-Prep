
# Looping Through a Dictionary

# 6.4

glossary = {
    'Indentation': 'Indentation refers to the spaces at the beginning of a code line',
    'Comments': 'Comments are code lines that will not be executed',
    'Camel Case': 'Camel Case Variable Names',
    'Numbers': 'There are three numeric types in Python',
    'Operators': 'Use operator to perform operations in Python'
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

