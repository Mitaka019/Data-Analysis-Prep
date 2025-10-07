
# Organizing a List

# 3.8

places = ['The Park', 'Bikini Bottom', 'Death Star', 'Citadel', 'Krasty Krabb']

print("Original Order:")
print(places)

print("\nSorted Order:")
print(sorted(places))

print("\nOriginal Order Again:")
print(places)

print("\nReverse Sorted Order:")
print(sorted(places))

print("\nOriginal Order Again:")
print(places)

print("\nOriginal to Reverse Order:")
places.reverse()
print(places)

print("\nReverse to Original Order:")
places.reverse()
print(places)

print("\nSort Order:")
places.sort()
print(places)

print("\nReverse Sort Order:")
places.sort(reverse=True)
print(places)

# 3.9

guests = ['mordecai', 'rigby', 'muscle man']
print(len(guests))