print(r'''
                                ____...------------...____
                           _.-"` /o/__ ____ __ __  __ \o\_`"-._
                         .'     / /                    \ \     '.
                         |=====/o/======================\o\=====|
                         |____/_/________..____..________\_\____|
                         /   _/ \_     <_o#\__/#o_>     _/ \_   \\
                         \_________       \####/       _________/         
                          |===\!/========================\!/===|
                          |   |=|          .---.         |=|   |
                          |===|o|=========/     \========|o|===|
                          |   | |         \() ()/        | |   |
                          |===|o|======{'-.) A (.-'}=====|o|===|
                          | __/ \__     '-.\uuu/.-'    __/ \__ |
                          |====          .'.'^'.'.         ====|
                          |  _\o/   __  {.' __  '.} _   _\o/  _|
                          `"""""""""""""""""""""""""""""""-""""` 
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n").lower()

    if choice2 == 'wait':
        choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()

        if choice3 == "blue":
            print("Congratulations! you found the treasure worth $10 million")
        elif choice3 == "red":
            print("You fell into hot lava.")
            print("Game Over :(")
        elif choice3 == "yellow":
            print("You got stung by bees.")
            print("Game Over :(")
        else:
            print("Wrong Door :(")
            print("Game Over :(")

    else:
        print("The piranhas in the lake ate you.")
        print("Game Over :(")

else:
    print("You fell into a hole.")
    print("Game Over :(")

