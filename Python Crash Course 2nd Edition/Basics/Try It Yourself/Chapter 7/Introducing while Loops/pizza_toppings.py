
# Introducing while Loops

# 7.4

prompt = "\nEnter a pizza topping you want:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")

