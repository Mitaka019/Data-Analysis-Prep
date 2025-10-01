
# Conditional Tests

# Checking for Equality

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

# Ignoring Case When Checking for Equality

car = 'Audi'
print(car == 'audi')

# You can use the lower() method to avoid the case.

car = 'Audi'
print(car.lower() == 'audi')

# It won't affect the value of the string.

print(car)