
# if Statements

# 5.6

age = 12

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"Your stage in life is {stage}.")

# 5.7

favorite_fruits = ['banana', 'apple', 'grapes']

if 'banana' in favorite_fruits:
    print("I love eating bananas.")
if 'apple' in favorite_fruits:
    print("I love eating apple.")
if 'oranges' in favorite_fruits:
    print("I love eating oranges.")
if 'lemon' in favorite_fruits:
    print("I love eating lemon.")
if 'grapes' in favorite_fruits:
    print("I love eating grapes.")