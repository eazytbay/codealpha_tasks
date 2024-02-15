# Select a random word
import random
from hangman_art import logo, stages
from guess_words import word_dict

chosen_word = random.choice(word_dict)

# Created a variable to keep track of number of lives of users
lives = 6

# Displays the name of game as a welcome logo
print(logo)

# Create a blank like a list
display = []
for letter in chosen_word:
    display.append('_')

# Use a while loop there are blanks in the in word
while '_' in display:

    # prompt the user to guess a word
    choose_word = input("Guess a letter: ").lower()

    if choose_word in display:
        print(f"Hmmm, I think you already guessed the letter '{guess}' ...")

    # Show if the letter entered was a correct guess
    for index, letter in enumerate(chosen_word):
        if letter == choose_word:
            display[index] = choose_word
    # Display the user's guess on the screen

    # if the letter guessed by the user is not in the list of
    # word, the number of lives is reduced and the hangman is updated
    if not choose_word in chosen_word:
        print("Ooops o_O that's a wrong letter, you just lost a life :(")
        lives -= 1
        print(stages[lives])

    # once the lives is reduced to 0 display game over and exit
    if lives == 0:
        print(f'Game Over, the correct word was {chosen_word}')
        break

    # At each correct stage, join the elements into a string separated by spaces and print
    print(f"{' '.join(display)}")

# if we have some lives left and we got rid of all the _ we win!
if lives != 0:
    print('Congratulations, You win!')

