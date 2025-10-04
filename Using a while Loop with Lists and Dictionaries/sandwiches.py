
# Using a while Loop with Lists and Dictionaries

# 7.8

sandwich_orders = ['pastrami', 'chicken', 'tuna', 'pastrami', 'egg', 'pastrami'] 
finished_sandwiches = []

# Making sandwiches until there are no more orders.

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Display all the finished wandwiches.
print("\nThe following sandwiches users have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")

