import gspread
from google.oauth2.service_account import Credentials
import random
import os
import datetime
import colorama
from colorama import Fore
from hangman_typing import *
from hangman_art import *
from hangman_words import word_list

# API for Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Authentification
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')
scores = SHEET.worksheet('scores')

# CONSTS
CORRECT_LETTER_SCORE = 10
EXTRA_SCORE = 100
FULL_WORD_SCORE = 500
repeat_message = f"""{Fore.CYAN}You have 3 choices:\n
A - PLAY AGAIN
B - LEADERBOARD
C - ESCAPE GAME
"""
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

# Add date to google worksheet
date = datetime.datetime.today()
today_date = date.strftime("%d/%m/%Y")

# Add color to text
colorama.init(autoreset=True)


def welcome_message():
    """Collect User´s name and city and set them as global variables
    so that they can be called in another funtion.
    """
    global player_name, player_city
    print(f'{Fore.GREEN}\t{logo}')
    typewriter("""It is 3 am and you are lost on a deserted train station somewhere
on your round trip to Europe.
Suddenly three bandits appear.... ! !""")
    print("\n")
    print(f"{Fore.YELLOW}And they ask...\n")

    # Collect player´s name and city
    if __name__ == '__main__':
        while True:
            player_name = input(f"{Fore.CYAN}What " +
                                "is your name?\n").strip().lower()
            if len(player_name) == 0:
                print(f"{Fore.RED}Invalid input!")
                continue
            else:
                break
        while True:
            player_city = input(f"{Fore.CYAN}What city " +
                                "are you originally from?\n").strip().lower()
            if len(player_city) == 0:
                print(f"{Fore.RED}Invalid Input!")
                continue
            else:
                break

    typewriter(""" You have 6 attempts to guess the city we are in now!
If you win, we let you go, if not you are coming with us!""")
    clean()
    print(f"{Fore.CYAN} HERE ARE THE RULES: {game_info[0]}")
    print(input("Press enter to start the game\n"))
    clean()


def play_game(chosen_word):
    """Main Hangman Game
    """
    chosen_word = random.choice(word_list).lower()
    # create blank
    word_length = "_" * len(chosen_word)

    correct_letters = []
    guessed_word = []
    wrong_letter_list = []
    guessed_right = 0
    score = 0
    attempts = 6
    global end_of_game
    end_of_game = False

    print(f"{Fore.YELLOW}YOU HAVE TO GUESS A WORD WITH "
          f"{len(chosen_word)} LETTERS !")
    print('\n')
    word_dash(word_length)
    print("\n")

    while not end_of_game:
        if wrong_letter_list != []:
            print(f'{Fore.RED}Wrong letters: {wrong_letter_list}')
            print('\n')
        guess = input("Guess a letter or word:  \n").lower()
        clean()

        if len(guess) == 1 and guess.isalpha():
            # prompts for already guessed letter
            if guess in word_length:
                print(f"You´ve already guessed {guess} correctly")

            elif guess in chosen_word:
                print(f"Great, {guess} is in the word!")
                correct_letters.append(guess)
                guessed_right += 1
                score += CORRECT_LETTER_SCORE

            # Make chosen word to a list
            word_as_list = list(word_length)
            indices = [
                i for i, letter in enumerate(chosen_word)
                if letter == guess
            ]
            for index in indices:
                word_as_list[index] = guess
            word_length = "".join(word_as_list)

            # check if user has got all letters.End of game.
            if "_" not in word_as_list:
                end_of_game = True
                print("You win!")
                score += EXTRA_SCORE

            # check if letter is wrong.
            if guess in wrong_letter_list:
                print(f"You´ve already guessed {guess} wrongly")
            elif guess not in chosen_word:
                wrong_letter_list.append(guess)
                print(f"You guessed {guess}, that´s not in the word.")

                attempts -= 1

                if attempts == 0:
                    end_of_game = True
                    print("You lose.\n")
                    print(f"{Fore.YELLOW}The word was {chosen_word}\n")

        # check for word inputs
        elif len(guess) >= 2 and guess.isalpha():
            if guess == chosen_word:
                end_of_game = True
                print(f"{Fore.YELLOW}\nWhoohh,You have guessed the word "
                      f"{guess} already!!!\nYou Win!!\n")
                score += FULL_WORD_SCORE - score

            elif guess in guessed_word:
                print(f"{Fore.RED}\nYou´ve already guessed {guess} wrongly")

            else:
                print(f"{Fore.RED}\n{guess}, is not the Word, try again!")
                attempts -= 1
                guessed_word.append(guess)
                if attempts == 0:
                    end_of_game = True
                    print("\tYou lose.\n")
                    print(f"{Fore.YELLOW}The word was {chosen_word}\n")

        else:
            print(f"{Fore.RED}\nINVALID INPUT!\n")

        word_dash(word_length)
        print("\n")
        print(f'Attempts left: {attempts}')
        print(f"Score: {score}")

        # import stages of hangman
        from hangman_art import stages
        current_stage = stages[attempts]
        lines = current_stage.split('\n')
        for line in lines:
            print(f"{line}")

    update_worksheet(player_name, player_city, today_date, score)
    repeat_game()
    clean()


def clean():
    """To clear the screen after every iteration
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def word_dash(word_length):
    """print out empty spaces for the letters of chosen word
    """
    print("", end="")
    for i in word_length:
        print(i, end=" ")
    print()


def repeat_game():
    """Asks the user if they want to play again or not.
    """
    while end_of_game:
        user_choice = input(f'{repeat_message}>>>').upper()
        if user_choice == 'A':
            clean()
            print(f'{Fore. YELLOW}{player_name.capitalize()}, ohh ' +
                  'whooh you have choosen to continue playing!')

            play_game(chosen_word)
        elif user_choice == 'B':
            clean()
            print(f'{Fore.YELLOW}Here are the scores of the top 5 players:\n')
            display_leaderboard()
        elif user_choice == 'C':
            typewriter(""" You are lucky to have escaped on the oncoming train....
See you later, alligator...""")
            print("\n")
            os.sys.exit()
        else:
            print('Please enter a valid answer')


def get_current_score(player_name):
    """Retrieve the current score of the player from the leaderboard
    """
    all_scores = scores.get_all_records()
    for record in all_scores:
        if record['NAME'] == player_name and record['CITY'] == player_city:
            return int(record['SCORE'])
    return 0


def update_worksheet(player_name, player_city, today_date, new_score):
    """Append the data from the player to the google worksheet.
       Add the endscores from end of game and other data from user
       to worksheet(scores)
    """
    all_records = scores.get_all_records()
    player_found = False
    for index, record in enumerate(all_records):
        if record['NAME'] == player_name and record['CITY'] == player_city:
            updated_score = int(record['SCORE']) + new_score
            scores.update_cell(index + 2, 4, updated_score)
            player_found = True
            current_score = get_current_score(player_name)
            print(f'{Fore.YELLOW}Your cumulative score is: {current_score}')
            break

    if not player_found:
        scores.append_row([player_name, player_city, today_date, new_score])
    print("Leaderboard updated.\n")


def display_leaderboard():
    """ To sort the score sheet according to score column
        in ascending order and display top five Players.
    """
    scores = SHEET.worksheet('scores')
    all_data = scores.get_all_values()
    sorted_data = sorted(all_data[1:], key=lambda x: int(x[3]),
                         reverse=True)[:5]
    header = f"{Fore.GREEN}{'Rank':<6}{'Name':<10}{'City':<15}{'Score':>10}"
    print(header)
    print(f"{Fore.YELLOW}{'='*45}\n")
    for i in range(0, len(sorted_data)):
        rank = i + 1
        name = sorted_data[i][0].capitalize()
        score = sorted_data[i][3]
        city = sorted_data[i][1].capitalize()
        row = f"{Fore.GREEN}{rank:<6}{name:<10}{city:<15}{score:>10}"
        print(row)

    print(f"{Fore.YELLOW}\n{'='*45}\n")


def main():
    """Main Function.
    """
    welcome_message()
    play_game(chosen_word)
    repeat_game()


if __name__ == '__main__':
    main()
