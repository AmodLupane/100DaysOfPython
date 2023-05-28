print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

per_head = (round(bill*(tip_percent/100) / split, 2)) + (round(bill/split, 2))

print(f"Each person should pay: ${per_head}")

