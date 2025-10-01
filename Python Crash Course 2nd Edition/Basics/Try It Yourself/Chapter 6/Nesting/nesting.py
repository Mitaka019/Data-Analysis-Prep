
# Nesting

# 6.7

people_0 = {'first': 'rachel joy', 'last': 'matudio', 'age': 22, 'city': 'quezon city'}
people_1 = {'first': 'mark jven', 'last': 'adriano', 'age': 22, 'city': 'montalban, rizal'}
people_2 = {'first': 'clarence', 'last': 'robedillo', 'age': 21, 'city': 'quezon city'}

people = [people_0, people_1, people_2]

for person in people:
    for person, info in person.items():
        print(f"{person}:{info}")
    print("\n")

# 6.8

pet_0 = {'owner': 'spongebob', 'pet': 'snail'}
pet_1 = {'owner': 'rigby', 'pet': 'raccoon'}
pet_2 = {'owner': 'patrick', 'pet': 'rock'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"The {pet['pet']} is owned by {pet['owner'].title()}.")

# 6.9

favorite_places = {
     "SpongeBob": ['bikini bottom', 'krasty krabb'],
    "Mickey Mouse": ['disney'],
    "Bugs Bunny": ['carrot farm', 'usa'],
    "Doraemon": ['japan', 'house of nobita'],
    "Jerry": ["tom's house", 'usa']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")

# 6.10

favorite_numbers = {
    "SpongeBob": [1, 0, 8, 5],
    "Mickey Mouse": [1, 3],
    "Bugs Bunny": [23, 6, 9],
    "Doraemon": [1],
    "Jerry": [7, 42, 0]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")

# 6.11

cities = {
    'Beijing': {
        'country': 'China',
        'population': 21.8,
        'fact': 'One of the oldest city in the world.'
    },
    'New York':{
        'country': 'USA',
        'population': 8.14,
        'fact': 'Business center of the United States.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 14,
        'fact': 'One of the densest city in the world.'
    },
}

for city, city_info in cities.items():
    print(f"{city.title()} is found in {city_info['country']} and has a population of {city_info['population']} million.")
    print(f"\n- Fun fact about it is:"
          f"{city_info['fact']}")
    print("\n")