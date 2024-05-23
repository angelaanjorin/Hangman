
import awoc
import random
import os
import datetime
import colorama
from colorama import Fore
colorama.init(autoreset = True)
from hangman_typing import *
from hangman_art import *

# to clean screen after each loop with change
def clean():
#on Windows System
    if os.name == 'nt':
        os.system('cls')
# on macOS and Linux System
    else:
        os.system('clear') 

my_world = awoc.AWOC()
nations_of_europe = my_world.get_countries_list_of ('Europe')
chosen_nation = random.choice(nations_of_europe).lower()
word_length = len(chosen_nation)
#print(nations_of_europe)

end_of_game = False
lives = 6

wrong_letter_list = []

#import logo
#from hangman_art import logo
print(f'{Fore.GREEN} {logo}')
typewriter ("""Y O U  A R E  B R A V E   T O  P L A Y\t\nT H I S   G A M E   B Y   T H E   W A Y ! !
\t\n\nG O O D   L U C K ! !\n
""")

#Testing code
print(f'Pssst...The chosen nation is {chosen_nation}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    if wrong_letter_list != []:
        print(f'Wrong letters: {wrong_letter_list}')
    guess = input("Guess a letter: ").lower()
    clean()

    #prompts for already guessed letter
    if guess in display:
        print(f"You´ve alread guessed {guess}")

    elif guess in chosen_nation:
        print(f"Great, {guess} is in the word! Keep going!")
    
        
    #check guessed letter
    for position in range(word_length):
        letter = chosen_nation[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #check if letter is wrong.
    if guess in wrong_letter_list:
        print(f"You´ve already guessed {guess}")
    elif guess not in chosen_nation:
        wrong_letter_list.append(guess)
        print(f"You guessed {guess}, that´s not in the word. You lose a life.")

        lives -= 1
    

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_nation}")

    print(f"{' '.join(display)}")

    print(f'Lives left: {lives}')
    
    #check if user has got all letters.End of game.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #import stages of hangman
    from hangman_art import stages
    print(stages[lives])
    