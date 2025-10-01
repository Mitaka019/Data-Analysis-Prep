
# What Is a List?

# A list is a collection of items in a particular order.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Index Positions Start at 0, Not 1

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# You can access the end of the list by making the index negative.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# Using Individual Values from a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)