
import awoc
import random
import os
#clear = lambda: os.system('cls') #on Windows System
#j
#os.system('clear') #on Linux System

my_world = awoc.AWOC()
nations_of_europe = my_world.get_countries_list_of ('Europe')
chosen_nation = random.choice(nations_of_europe).lower()
word_length = len(chosen_nation)

end_of_game = False
lives = 6

wrong_letter_list = []

#import logo
from hangman_art import logo
print(logo)


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
    #clear()

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
    