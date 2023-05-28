import random

names_string = input("Enter everybody's names separted by comma.\n")

names = names_string.split(", ")

payer = random.randint(0, len(names)-1)

print(f"{names[payer]} is going to buy the meal today!")

# The above work can be done using the choice() function
# payer = random.choice(names)