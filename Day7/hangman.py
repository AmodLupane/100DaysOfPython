import random
import hangman_asciiArt
import hangman_words

print(hangman_asciiArt.logo)

chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)

display = []
for i in range(word_len):
    display.append("_")

lives = 7
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter : ").lower()

    if guess in display:    # If the letter has already been guessed
        print("You have already guessed the letter.")
    else:   # If not check in the for the letter in the word
        for position in range(word_len):
            if chosen_word[position] == guess:
                display[position] = guess
        print(' '.join(display))    # To print list as string
        print() # For new line
        if (lives < 7): # To keep printing the man after 1 miss has occurred.
            print(hangman_asciiArt.stages[lives])    
            print()   

    if guess not in chosen_word:
        print(f"'{guess}' is not present in the word. You lose a life.")
        print("------------------------------------------------")
        lives -= 1
        print(hangman_asciiArt.stages[lives])
        print()
        if lives == 0:
            end_of_game = True
            print("You Lose :(")

    if "_" not in display:
        end_of_game = True
        print("You Won!")
