
import random
word_list = ["amsterdam", "barcelona", "helsinki"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The chosen word is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    
    #check if there are no more empty spaces left in display. Then all letters have been guessed correctly. End of game.
    if "_" not in display:
        end_of_game = True
        print("You win!")