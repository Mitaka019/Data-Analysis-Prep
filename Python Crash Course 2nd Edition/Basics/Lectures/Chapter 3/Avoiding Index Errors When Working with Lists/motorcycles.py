
# Avoiding Index Errors When Working with Lists

motorcycles = ['honda', 'yamaha', 'suzuki'] 
#print(motorcycles[3])

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[-1])

# This will only cause an error if the list is empty.

motorcycles = []
#print(motorcycles[-1])
