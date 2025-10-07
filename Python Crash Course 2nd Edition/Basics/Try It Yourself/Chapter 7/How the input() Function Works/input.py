
# How the input() Function Works

# 7.1

prompt = input("Hello, how may I help you today? What car would you like to rent? ")
print(f"Let me see if we have the {prompt.title()}. Thank you!")

# 7.2

prompt = "Hi there, can I interest you to our menu tonight? "
prompt += "How many are you eating for tonight? "

order = int(input(prompt))

if order < 8:
    print(f"\nWe'll be preparing your sit in a moment. Please follow me.")

else:
    print(f"\nSorry, you'll have to wait for a couple of minutes due to lack of seats. Thank you!")

# 7.3

prompt = input("\nGive me a number and I'll tell you if it's a multiple of 10. ")

prompt = int(prompt)

if prompt % 10 == 0:
    print(f"{prompt} is a multiple of 10.")
else:
    print(f"{prompt} is not a multiple of 10.")