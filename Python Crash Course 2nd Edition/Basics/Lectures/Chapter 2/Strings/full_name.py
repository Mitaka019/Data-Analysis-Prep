
# Strings

# Using Variables in Strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# These strings are called f-strings.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

# In programming, whitespace refers to any nonprinting character, such as
# spaces, tabs, and end-of-line symbols.

print("Python")

print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

# You can combine both tabs and newlines.

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

# To permanently remove the whitespace.

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# 