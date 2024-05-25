
#import awoc
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

import random
import os
#import datetime

import colorama
from colorama import Fore
colorama.init(autoreset = True)

from hangman_typing import *
from hangman_art import *
from hangman_words import word_list

#CONSTS
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')

scores = SHEET.worksheet('scores')

data = scores.get_all_values()

#print(data)
CORRECT_LETTER_SCORE = 5
EXTRA_SCORE = 20
FULL_WORD_SCORE = 50


#Collect name and city from the user
#Add date and time to scores
#Add the calculated scores from end of game to scores
#Retrieve and show user thier scores
# Ask user if they want to see the top five scored users

#import logo
#from hangman_art import logo
def welcome_message():
    print(f'{Fore.GREEN} {logo}')
    typewriter (""" W E L C O M E   T O  T H E  H A N G M A N  G A M E ! !\n """)
    print(f"{Fore.CYAN} HERE ARE THE RULES: {game_info[0]}")
    print(input("Press enter to start the game\n"))
    clean()
    #while True:
        #if play_game:
            #chosen_word = random.choice(word_list).lower()
        #play_game == input("Do you want to play? Y/N\n").lower()
        #if play_game == "y":
            #print(f"{Fore.GREEN} GREAT LET`S PLAY!\n")
        # play_game = True
        #elif play_game == "n":
            #print(f"{Fore.YELLOW} OKAY, MAYBE NEXT TIME!")
            #sys.exit()
        #else:
            #print(f"{Fore.RED}Invalid input. Please try again")
            #play_game = False
    if __name__ == '__main__':
        while True:
            player_name = input(f"{Fore.CYAN}Please enter your name:\n").strip().lower()
            if len(player_name) == 0:
                print(f"{Fore.RED}Invalid input!")
                continue
            else:
                break
        while True:
            player_city = input(f"{Fore.CYAN}Please enter your city:\n").strip().lower()
            if len(player_name) == 0:
                print(f"{Fore.RED}Invalid input!")
                continue
            else:
                break
    typewriter (""" Y O U  A R E  B R A V E   T O  P L A Y\t\nT H I S   G A M E   B Y   T H E   W A Y ! !
    \t\n\nG O O D   L U C K ! !\n
    """)
    clean()
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
def play_game(chosen_word):
    #Testing code
    print(f'Pssst...The chosen nation is {chosen_word}.')

    word_length = "_"  * len(chosen_word)
    #create blanks
    def word_dash(word_length):
        for i in word_length:
            print(i, end=" ")
    #for _ in range(word_length):
    # display += "_"

    #print(nations_of_europe)
    correct_letters = []
    guessed_word = []
    wrong_letter_list = []
    guessed_right = 0
    score = 0
    end_of_game = False
    attempts = 6

    print(f"""{Fore.YELLOW}YOU HAVE TO GUESS A WORD WITH {len(chosen_word)} LETTERS""")
    print('\n')
    word_dash(word_length)
    print("\n")

    while not end_of_game:
        if wrong_letter_list != []:
            print(f'{Fore.RED}Wrong letters: {wrong_letter_list}')
            print('\n')
        guess = input("Guess a letter: ").lower()
        clean()

        if len(guess) == 1 and guess.isalpha():
        #prompts for already guessed letter
            if guess in word_length:
                print(f"You´ve already guessed {guess} correctly")

            elif guess in chosen_word:
                print(f"Great, {guess} is in the word!")
                correct_letters.append(guess)
                guessed_right += 1
                score += CORRECT_LETTER_SCORE
   
            #check guessed letter
            word_as_list = list(word_length)
            indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_length = "".join(word_as_list)

            #check if user has got all letters.End of game.
            if "_" not in word_as_list:
                end_of_game = True
                print("You win!")
                repeat_game()

            #for position in range(word_length):
                #letter = chosen_word[position]
                #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
                #if letter == guess:
                    #display[position] = letter

            #check if letter is wrong.
            if guess in wrong_letter_list:
                print(f"You´ve already guessed {guess} wrongly")
            elif guess not in chosen_word:
                wrong_letter_list.append(guess)
                print(f"You guessed {guess}, that´s not in the word.")

                attempts -= 1

                if attempts == 0:
                    end_of_game = True
                    print("You lose.")
                    print(f"The word was {chosen_word}")
                    repeat_game()
                    
        #check for word inputs
        elif len(guess) >= 2  and guess.isalpha():
            if guess == chosen_word:
                end_of_game = True
                print(f"""{Fore.YELLOW}\n Whoohh,You have guessed the word {guess} already!!!\n You Win!!\n""")
                score += FULL_WORD_SCORE
                repeat_game()
            elif guess in guessed_word:
                print(f"{Fore.RED}\n\t You´ve already guessed {guess} wrongly")
            
            elif guess != chosen_word:
                print(f"{Fore.RED}\n\t{guess}, is not the Word, try again!")
                attempts -= 1
                guessed_word.append(guess)
            
            else:
                end_of_game = True
                word_length = chosen_word
        else:
            print(f"{Fore.RED}\n\t INVALID INPUT!\n")

        #print(f"{' '.join(word_as_list)}")
        word_dash(word_length)
        print("\n")
        print(f'Attempts left: {attempts}')
        #print("\n")
        print(f"Score: {score}")
        

        #import stages of hangman
        from hangman_art import stages
        print(stages[attempts])

def repeat_game():
    """Asks the user if they want to play again or not.
    """
    game = input('Are you ready to play again? Y(es) or N(o)\n').upper()
    if game == 'Y':
        clean()
        play_game(chosen_word)
    elif game == 'N':
        print('Goodbye!')
        sys.exit()
    else:
        print('Please enter a valid answer')
        repeat_game()




def main():
    welcome_message()
    play_game(chosen_word)
    repeat_game()
main()
