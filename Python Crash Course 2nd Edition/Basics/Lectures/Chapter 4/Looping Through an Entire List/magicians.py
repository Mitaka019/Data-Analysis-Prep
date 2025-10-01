
# Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# You can also write as many lines of code as you like in the for loop. 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")

# Doing Something After a for Loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")

print("Thank you, everyone. That was a great magic show!")
