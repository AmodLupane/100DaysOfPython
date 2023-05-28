print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm : "))

if height > 120:
    print("You can ride the rollercoaster.")

    age  = int(input("Enter your age : "))

    if age > 18:
        bill  = 12
        print("The ticket cost for adults is $12.")
    elif age >= 45 and age <=55:
        bill = 0
        print("Everything is okay, please have a free ride with us.")
    elif age > 12:
        bill = 10
        print("The ticket cost for teens is $10.")
    else:
        bill = 7
        print("The ticket cost for childer is $7.")
    
    want_photos = input("Do you want photos? Y or N. ")
    if want_photos == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you ride.")