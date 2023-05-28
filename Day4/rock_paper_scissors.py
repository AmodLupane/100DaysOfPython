import random

rock = '''
   _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___) 

'''

paper = '''
 _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)

'''

scissors = '''
 _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

'''
choices = [rock, paper, scissors]

user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>2 or user_choice<0:
    print("Invalid input. You lose.")
else:
    print(f"You chose :")
    print(choices[user_choice])
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose :")
    print(choices[computer_choice])
    
    if user_choice==0 and computer_choice==2:
        print("You Win!")
    elif computer_choice==0 and user_choice==2:
        print("Computer Wins!")
    elif computer_choice > user_choice:
        print("Computer Wins!")
    elif computer_choice < user_choice:
        print("You Win!")
    elif user_choice == computer_choice:
        print("Draw")
    else:
        print("Invalid Input")