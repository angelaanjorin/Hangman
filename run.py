
#import awoc
import random
import os
import datetime
import colorama
from colorama import Fore
colorama.init(autoreset = True)
from hangman_typing import *
from hangman_art import *
from hangman_words import word_list

#import logo
#from hangman_art import logo
print(f'{Fore.GREEN} {logo}')
typewriter ("""Y O U  A R E  B R A V E   T O  P L A Y\t\nT H I S   G A M E   B Y   T H E   W A Y ! !
\t\n\nG O O D   L U C K ! !\n
""")

# To clear the screen after every iteration
def clean():
#on Windows System
    if os.name == 'nt':
        os.system('cls')
# on macOS and Linux System
    else:
        os.system('clear') 

#my_world = awoc.AWOC()
#nations_of_europe = my_world.get_countries_list_of ('Europe')
chosen_word = random.choice(word_list).lower()
#get_word ()

#Testing code
print(f'Pssst...The chosen nation is {chosen_word}.')

word_length = "_"  * len(chosen_word)
#print(nations_of_europe)
display = []
guessed_word = []
wrong_letter_list = []
end_of_game = False
attempts = 6



#create blanks
def word_dash(word_length):
    for i in word_length:
        print(i, end=" ")
#for _ in range(word_length):
   # display += "_"


while not end_of_game:
    if wrong_letter_list != []:
        print(f'Wrong letters: {wrong_letter_list}')
    guess = input("Guess a letter: ").lower()
    clean()

    #prompts for already guessed letter
    if guess in display:
        print(f"You´ve already guessed {guess}")

    elif guess in chosen_word:
        print(f"Great, {guess} is in the word!")
    
        
    #check guessed letter
    word_as_list = list(word_length)
    indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    word_length = "".join(word_as_list)

    #for position in range(word_length):
        #letter = chosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        #if letter == guess:
            #display[position] = letter

    #check if letter is wrong.
    if guess in wrong_letter_list:
        print(f"You´ve already guessed {guess}")
    elif guess not in chosen_word:
        wrong_letter_list.append(guess)
        print(f"You guessed {guess}, that´s not in the word.")

        attempts -= 1
    

        if attempts == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    #print(f"{' '.join(word_as_list)}")
    word_dash(word_length)

    print(f'Attempts left: {attempts}')
    
    #check if user has got all letters.End of game.
    if "_" not in word_as_list:
        end_of_game = True
        print("You win!")

    #import stages of hangman
    from hangman_art import stages
    print(stages[attempts])
