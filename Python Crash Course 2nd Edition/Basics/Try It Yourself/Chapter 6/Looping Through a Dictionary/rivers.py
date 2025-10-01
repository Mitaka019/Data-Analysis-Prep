
# Looping Through a Dictionary

# 6.5

rivers = {
    'nile': 'egypt',
    'yellow': 'china',
    'indus': 'pakistan'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through the {country.title()}.")

print("\nThe following river has been mentioned:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following country has been mentioned:")
for country in rivers.values():
    print(f"- {country.title()}")

