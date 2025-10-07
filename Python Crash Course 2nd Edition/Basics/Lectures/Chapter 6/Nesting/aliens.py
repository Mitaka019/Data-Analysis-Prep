
# Nesting

# Sometimes you’ll want to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This is called nesting.

# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A more realistic example would involve more than three aliens with
# code that automatically generates each alien.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_numebr in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Imagine that one aspect of a game has some aliens changing color and moving faster as the
# game progresses.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_numebr in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium' 
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# You could expand this loop by adding an elif block that turns yellow
# aliens into red, fast-moving ones worth 15 points each.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_numebr in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'medium'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium' 
            alien['points'] = 10
    elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")