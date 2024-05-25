stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

         
game_info = [
 # hangman game rules
 """
    _________________________________________________________________________
   |   ___________________________________________________________________   |
   |  |                                                                   |  |
   |  |                ===============================                    |  |
   |  |                | |                         | |                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                | |                         | |                    |  |
   |  |                ===============================                    |  |
   |  |                                                                   |  |
   |  |  1 - You have 6 attempts to try to find the right word by         |  |
   |  |      inputting letters or the full word                           |  |
   |  |  2 - If you guess a wrong letter you will lose an attempt and the |  |
   |  |      hangman will begin building                                  |  |
   |  |  3 - When you reach 0 attempts you will be hanged - Game Over     |  |
   |  |  POINTS:                                                          |  |
   |  |  * 5 points per letter guessed right                              |  |
   |  |  * 20 points if you guessed the right word                        |  |
   |  |  * 50 extra points to complete the full word with max 3 letters   |  |
   |  |    already guessed.                                               |  |
   |  |___________________________________________________________________|  |
   |_________________________________________________________________________|
"""]                                                      
                                                                    