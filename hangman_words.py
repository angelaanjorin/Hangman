import random

word_list = [
    "Lisbon",
    "Barcelona",
    "Prague",
    "Berlin",
    "Stockholm",
    "Helsinki",
    "Istanbul",
    "Moscow",
    "London",
    "Madrid",
    "Rom",
    "Kiev",
    "Paris",
    "Vienna",
    "Minsk",
    "Hamburg",
    "Warsaw",
    "Bucharest",
    "Belgrade",
    "Copenhagen",
    "Brussels",
    "Athens",
    "Budapest",
    "Munich",
    "Frankfurt",
    "Milan",
    "Birmingham",
    "Manchester",
    "Sofia",
    "Dublin",
    "Bern",
    "Chisinau",
    "Bratislava",
    "Ljubljana",
    "Luxembourg",
    "Monaco",
    "Nicosia",
    "Nuuk",
    "Oslo",
    "Podgorica",
    "Reykavik",
    "Serajevo",
    "Tallinn",
    "Tirana",
    "Vaduz",
    "Valletta",
    "Vatican",
    "Vilnius",
    "Zagreb"
]

"""Choose a word randomly from the word list
"""
def get_word ():
    chosen_word = random.choice(word_list)
    return chosen_word.lower()