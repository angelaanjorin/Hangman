import gspread
from google.oauth2.service_account import Credentials
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


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#CONSTS
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')

scores = SHEET.worksheet('scores')
data = scores.get_all_values()

CORRECT_LETTER_SCORE = 10
EXTRA_SCORE = 100
FULL_WORD_SCORE = 500
repeat_message = f"""{Fore.CYAN}
A - PLAY AGAIN
B - LEADERBOARD
C - EXIT GAME
"""
chosen_word = random.choice(word_list).lower()
global word_length 
word_length = "_"  * len(chosen_word)
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

    #create blank
    
    correct_letters = []
    guessed_word = []
    wrong_letter_list = []
    guessed_right = 0
    score = 0
    attempts = 6
    global end_of_game 
    end_of_game = False
   
    print(f"""{Fore.YELLOW}YOU HAVE TO GUESS A WORD WITH {len(chosen_word)} LETTERS""")
    print('\n')
    word_dash()
    print("\n")

    while not end_of_game:
        if wrong_letter_list != []:
            print(f'{Fore.RED}Wrong letters: {wrong_letter_list}')
            print('\n')
        guess = input("Guess a letter: ").lower()
        clean()

        if len(guess) == 1 and guess.isalpha():
        #prompts for already guessed letter
            if guess in correct_letters:
                print(f"You´ve already guessed {guess} correctly")

            elif guess in chosen_word:
                print(f"Great, {guess} is in the word!")
                correct_letters.append(guess)
                guessed_right += 1
                score += CORRECT_LETTER_SCORE

            #Make chosen word to a list
            create_wordlist()

            #check if user has got all letters.End of game.
            if "_" not in word_as_list:
                end_of_game = True
                print("You win!")
                score += EXTRA_SCORE
                
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
                
        #check for word inputs
        elif len(guess) >= 2  and guess.isalpha():
            if guess == chosen_word:
                end_of_game = True
                print(f"""{Fore.YELLOW}\n Whoohh,You have guessed the word {guess} already!!!\n You Win!!\n""")
                score += FULL_WORD_SCORE - score
                
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

        
        word_dash()
        print("\n")
        print(f'Attempts left: {attempts}')
        #print("\n")
        print(f"Score: {score}")

        #import stages of hangman
        from hangman_art import stages
        print(stages[attempts])
    update_worksheet(data, player_name, player_city, today_date, score)

def get_word():
    """get a word for the game randomly from the word list and make it lowercase.
    """
    global chosen_word
    chosen_word = random.choice(word_list)
    return chosen_word.lower()

def word_dash():
    """print out empty spaces for the letters of chosen word
    """
    global word_length
    word_length = "_"  * len(chosen_word)
    for i in word_length:
        print(i, end=" ")


def create_wordlist():
    """creates a list for the number of letters in the chosen word.
    """
    word_as_list = list(word_length)
    indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    word_length = "".join(word_as_list)

#Repeat game      
def repeat_game():
    """Asks the user if they want to play again or not.
    """
    while end_of_game == True:
        user_choice = input(f'{repeat_message}>>>').upper()
        if user_choice == 'A':
            clean()
            print(f'{player_name.capitalize()}, ohh whoh you have choosen to continue playing!')
            chosen_word = random.choice(word_list).lower()
            #print(f"Score:{score}")
            play_game(chosen_word)
            #display_score(score)
        elif user_choice == 'B':
            clean()
            print('Here are the scores of the best 5 players... ')
            display_leaderboard()
            
        elif user_choice == 'C':
            print('Goodbye!')
            os.sys.exit()
        else:
            print('Please enter a valid answer')
            repeat_game()
        

def display_score(score):
    """Displays the user´s score during the game
    """
    print(f"\tSCORE: {score}")


#Add the endscores from end of game and other data from user to worksheet(scores)
def update_worksheet(data, player_name, player_city, today_date, score):
    """To append the data from the player to the google worksheet
    """
    print("Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet('scores')
    worksheet_to_update.append_row([str(player_name[0:10]), player_city, today_date, score])
    
    print('Leaderboard Updated.\n')

#displaying the data in worksheet to user
def display_player_score():
    """To retrieve the data from google sheet and display to user
    """
    print("Getting data....")
    scores = SHEET.worksheet("scores").get_all_values()
    scores_row = scores[-1]
    print(scores_row)

def display_leaderboard():
    """to sort the score sheet according to score column 
    in ascending order and displaying the last five.
    """
    scores = SHEET.worksheet('scores')
    columns =[]
    for ind in range(1,5):
        column = scores.col_values(ind)
        columns.append(column[-5])
        print(columns)


def sort_sheet():
    scores = SHEET.worksheet('scores')

    sorted_col_list = []
    sorted_col = scores.sort((4, 'asc'), range = 'A2:D92')
    sorted_list.append(sorted_col)
    print(f'Leaderboard: {sorted_col_list}')

#Main function
def main():
    """Main Function
    """
    welcome_message()
    play_game(chosen_word)
    repeat_game()
main()
