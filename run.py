
import awoc
import random

my_world = awoc.AWOC()
nations_of_europe = my_world.get_countries_list_of ('Europe')
chosen_nation = random.choice(nations_of_europe).lower()
word_length = len(chosen_nation)

end_of_game = False
lives = 6

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
    guess = input("Guess a letter: ").lower()

    #check guessed letter
    for position in range(word_length):
        letter = chosen_nation[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #check if letter is wrong.
    if guess not in chosen_nation:
        print(f"You guessed {guess}, that´s not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    
    #check if use has got all letters.End of game.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #import stages of hangman
    from hangman_art import stages
    print(stages[lives])
    