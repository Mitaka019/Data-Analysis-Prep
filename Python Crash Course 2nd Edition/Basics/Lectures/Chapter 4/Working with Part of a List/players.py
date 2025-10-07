
# Working with Part of a List

# Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# If you want the second, third, and fourth items in a list, you would start the slice at index 1 and
# end at index 4.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list. 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# If you want to show the last 3 players.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

