
# Making Numerical Lists

# 4.3

for value in range(1, 21):
    print(value)

# 4.4

million = []
for value in range(1, 1000001):
    million.append(value)

print(million)

# 4.5

million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

# 4.6

odd = []
for value in range(1, 21, 2):
    odd.append(value)

print(odd)

# 4.7 

threes = []

for value in range(3, 31, 3):
    threes.append(value)

print(threes)

# 4.8

cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)

print(cubes)

# 4.9

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

