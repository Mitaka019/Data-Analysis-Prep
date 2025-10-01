
# Looping Through a Dictionary

# Looping Through All Key-Value Pairs

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in favorite_languages.keys():
    print(name.title())

# You can access the value associated with any key you care about inside
# the loop by using the current key.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# You can also use the keys() method to find out if a particular person
# was polled.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

if 'erin' in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# To see each language without repitition, we can use the set function.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
