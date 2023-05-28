print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm : "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age : "))
    if age>18:
        print("You have to pay $12")
    elif age<7:
        print("You have to pay $7")
    else:
        print("You have to pay $10")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster")