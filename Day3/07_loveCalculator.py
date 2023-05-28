print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
combined_name_lower = combined_name.lower()

t = combined_name_lower.count("t")
u = combined_name_lower.count("u")
r = combined_name_lower.count("r")
e = combined_name_lower.count("e")
true = t + r + u + e

l = combined_name_lower.count("l")
o = combined_name_lower.count("o")
v = combined_name_lower.count("v")
e = combined_name_lower.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")


