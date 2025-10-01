
# Using if Statements with Lists

# 5.8

users = ['admin', 'clarence', 'rigby', 'rachel', 'spongebob']

for user in users:
    if user == 'admin':
        print("Thank you for logging in again admin, would you like to see a status report?")
    else:
        print(f"Thank you for logging in again {user}.")

# 5.9

users = []

if users:
    for user in users:
        if user == 'admin':
            print("Thank you for logging in again admin, would you like to see a status report?")
        else:
            print(f"Thank you for logging in again {user}.")

else:
    print(f"We need more users!!")

# 5.9

current_users = ['admin', 'clarence', 'rigby', 'rachel', 'spongebob']

new_users = ['Clarence', 'jven', 'Kristopher', 'marco', 'Spongebob']

for user in new_users:
    if user.lower() in current_users:
        print(f"\nI'm sorry {user}, your username has already been selected. Please choose another one.")
    else:
        print(f"Welcome {user.title()}, thank you for joining us!")
