import random

print("Welcome to PyPassword Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '-', '_', '+', '=']

num_letters = int(input("Enter the number of letter you want in your password : "))
num_symbols = int(input("Enter the number of symbols you want in your password : "))
num_numbers = int(input("Enter the number of numbers you want in your password : "))

password = []

for i in range(0, num_letters):
    password.append(random.choice(letters))
for i in range(0, num_symbols):
    password.append(random.choice(symbols))
for i in range(0, num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
str_password = ""

for letter in password:
    str_password += letter

print(str_password)