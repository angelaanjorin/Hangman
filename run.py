
import random
word_list = ["amsterdam", "Barcelona", "Helsinki"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The chosen word is {chosen_word}.')

guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("Wrong")