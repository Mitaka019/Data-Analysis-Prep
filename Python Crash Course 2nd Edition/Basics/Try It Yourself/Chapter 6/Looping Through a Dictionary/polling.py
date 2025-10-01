
# Looping Through a Dictionary

# 6.6

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['clarence', 'jven', 'sarah', 'kristopepe', 'phil']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Thank you for taking the poll {friend.title()}.")
    else:
        print(f"Please take the poll {friend.title()}.")