
# Changing, Adding, and Removing Elements

# 3.4

guests = ['mordecai', 'rigby', 'muscle man']
print(guests)

print(f"Hey {guests[0].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[1].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[2].title()}, would you like to attend to our dinner party tonight? Free of charge!")

# 3.5

print(f"\n{guests[2].title()}, won't be joining us tonight. So there'll be another one invited.")

guests[2] = 'benson'
print(guests)

print(f"Hey {guests[0].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[1].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[2].title()}, would you like to attend to our dinner party tonight? Free of charge!")

# 3.6

print(f"\nWe found a bigger table so there'll be 3 new guests invited.")

guests.insert(0, 'skips')
guests.insert(1, 'high five ghost')
guests.append('pops')

print(guests)

print(f"Hey {guests[0].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[1].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[2].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[3].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[4].title()}, would you like to attend to our dinner party tonight? Free of charge!")
print(f"Hey {guests[5].title()}, would you like to attend to our dinner party tonight? Free of charge!")

# 3.7

print(f"\nThe table won't arrive on time so there'll be 2 guests accomodated for the mean time.")

print(f"\nI'm sorry {guests.pop()}, please wait for your turn! Thank you!")
print(f"\nI'm sorry {guests.pop()}, please wait for your turn! Thank you!")
print(f"\nI'm sorry {guests.pop()}, please wait for your turn! Thank you!")
print(f"\nI'm sorry {guests.pop()}, please wait for your turn! Thank you!")

print(f"\n{guests[0].title()} and {guests[1].title()} you'll be the first two to be accomodated tonight. Follow me!")

del guests[1]
print(guests)

del guests[0]
print(guests)