
import random
word_list = ["amsterdam", "Barcelona", "Helsinki"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The chosen word is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("Wrong")