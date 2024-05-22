
import random
word_list = ["amsterdam", "barcelona", "helsinki"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The chosen word is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

print(display)