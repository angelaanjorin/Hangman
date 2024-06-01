import sys
import time


def typewriter(string):
    '''for the main text at the beginning of the game
    '''
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    # Pause after printing the entire sentence
    time.sleep(1)
