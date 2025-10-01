
# How the input() Function Works

# Writing Clear Prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input

age = input("How old are you? ")
print(age)

# To accept numerical input:

age = input("How old are you? ")
age = int(age)
print(age >= 18)

