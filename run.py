import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

import random
import os

#Add date to google worksheet
import datetime
date = datetime.datetime.today()
today_date = date.strftime("%d/%m/%Y")

#Add color to text 
import colorama
from colorama import Fore
colorama.init(autoreset = True)

from hangman_typing import *
from hangman_art import *
from hangman_words import word_list
chosen_word = random.choice(word_list).lower()

#CONSTS
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')

scores = SHEET.worksheet('scores')
data = scores.get_all_values()

CORRECT_LETTER_SCORE = 5
EXTRA_SCORE = 50
FULL_WORD_SCORE = 500
score = 0

# Retrieve and show user thier scores
# Ask user if they want to see the top five scored users

def welcome_message():
    """Collect User´s name and city and set them as global variables so that they can be called in another funtion.
    """
    global player_name, player_city
    #print(f'{Fore.GREEN} {logo}')
    #typewriter (""" W E L C O M E   T O  T H E  H A N G M A N  G A M E ! !\n """)
    #print(f"{Fore.CYAN} HERE ARE THE RULES: {game_info[0]}")
    #print(input("Press enter to start the game\n"))
    #clean()
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

    #Collect user´s name and city       
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
    #typewriter (""" Y O U  A R E  B R A V E   T O  P L A Y\t\nT H I S   G A M E   B Y   T H E   W A Y ! !
    #\t\n\nG O O D   L U C K ! !\n
   # """)
#     clean()

# To clear the screen after every iteration
def clean():
#on Windows System
    if os.name == 'nt':
        os.system('cls')
# on macOS and Linux System
    else:
        os.system('clear') 

#chosen_word = random.choice(word_list).lower()
# #get_word ()
def play_game(chosen_word):
    #Testing code
    print(f'{Fore.LIGHTMAGENTA_EX}Pssst...The chosen nation is {chosen_word}.')

    word_length = "_"  * len(chosen_word)
    #create blanks
    def word_dash(word_length):
        for i in word_length:
            print(i, end=" ")
    
    correct_letters = []
    guessed_word = []
    wrong_letter_list = []
    guessed_right = 0
    score = 0
    global end_of_game 
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
                print(f"The word was {chosen_word}")
                #print(f"Score:{score}")
                #repeat_game()

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
                    #repeat_game()

        #check for word inputs
        elif len(guess) >= 2  and guess.isalpha():
            if guess == chosen_word:
                end_of_game = True
                print(f"""{Fore.YELLOW}\n Whoohh,You have guessed the word {guess} already!!!\n You Win!!\n""")
                score += FULL_WORD_SCORE - score
                #print(f"Score:{score}")
                #repeat_game()
            elif guess in guessed_word:
                print(f"{Fore.RED}\n\t You´ve already guessed {guess} wrongly")
            
            elif guess != chosen_word:
                print(f"{Fore.RED}\n\t{guess}, is not the Word, try again!")
                attempts -= 1
                guessed_word.append(guess)
            
            else:
                end_of_game = True
                word_length = chosen_word
                score += EXTRA_SCORE
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
    update_worksheet(data, player_name, player_city, today_date, score)
#play_game(chosen_word)
#         #final_score(end_of_game, chosen_word, guessed_right, score)

# # def final_score(end_of_game, chosen_word, guessed_right, score):
# #     if end_of_game and len(chosen_word) >= 6 and guessed_right <=3:
# #         print("You win, You have guessed the word completely at once!\n")
# #         score = score + EXTRA_SCORE + FULL_WORD_SCORE
# #     elif end_of_game:
# #         print("You win, You have guessed the right word!\n")
# #         score = score + EXTRA_SCORE
# #     else:
# #         print(f"You lose, the right word was {chosen_word}\n")
# #     #update_worksheet(data, score)
# #     display_score(score)

def get_word():
    """get a word for the game randomly from the word list and make it lowercase.
    """
    global chosen_word
    chosen_word = random.choice(word_list)
    return chosen_word.lower()

#Repeat game      
def repeat_game():
    """Asks the user if they want to play again or not.
    """
    while end_of_game == True:
        game = input('Are you ready to play again? Y(es) or N(o)\n').upper()
        if game == 'Y':
            clean()
            chosen_word = random.choice(word_list).lower()
            #print(f"Score:{score}")
            play_game(chosen_word)
            display_score(score)
        elif game == 'N':
            print('Goodbye!')
            sys.exit()
        else:
            print('Please enter a valid answer')
    repeat_game()


def display_score(score):
    """Displays the user´s score during the game
    """
    print(f"\tSCORE: {score}")


#Add the endscores from end of game and other data from user to worksheet(scores)
def update_worksheet(data, player_name, player_city, today_date, score):
    
    print("Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet('scores')
    worksheet_to_update.append_row([str(player_name[0:10]), player_city, today_date, score])
    
    print('Leaderboard Updated.\n')

    #print(data)

#Main function
def main():
    welcome_message()
    play_game(chosen_word)
    #final_score(end_of_game, chosen_word, guessed_right, score)
    #update_worksheet(data, player_name, player_city, today_date, score)
    repeat_game()
main()
