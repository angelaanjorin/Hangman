stages = [
  '''\
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', 
    '''\
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
    '''\
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
    '''\
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
    '''\
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
    '''\
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
    '''\
  +---+
  |   |
      |
      |
      |
      |
========='''
]

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
                   """ 
      
game_info = [
 # hangman game rules
 """
    _________________________________________________________________________
   |   ___________________________________________________________________   |
   |  |                                                                   |  |
   |  |                     G A M E   R U L E S                           |  |
   |  |                                                                   |  |
   |  |  1 - You have 6 attempts to try to find the right word by         |  |
   |  |      inputting letters or the full word                           |  |
   |  |  2 - If your guess is wrong you will lose an attempt and the      |  |
   |  |      hangman will begin building                                  |  |
   |  |  3 - When you reach 0 attempts you will be hanged - Game Over     |  |
   |  |  POINTS:                                                          |  |
   |  |  * 10 points for every correct letter                             |  |
   |  |  * 500 points if you guessed the right word                       |  |
   |  |  * 100 points extra if you win by guessing the word               |  |
   |  |    letter for letter                                              |  |
   |  |___________________________________________________________________|  |
   |_________________________________________________________________________|
"""
]                                                      
                                                                    
# leaderboard = [
#    # hangman leaderbord
#  """
#                   L E A D E R B O A R D

#     =============================================
#         POS\tNAME\tSCORE\tCITY
#     =============================================
# """
# ]                                                                   