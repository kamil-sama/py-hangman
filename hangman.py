from random import choice as pick
import db
import random

dictionary = db.words['easy_difficulty']
secret = pick(dictionary)
guesses_taken = []
limit = 10

game_ended = bool(False)

def play():
    for attempt in range(1,limit):
        mystery = _doTheThing()
        print(mystery)

        if not game_ended:
            c = input(f"Please take a guess (letter or the word), attempts left: {10-attempt}")
            guesses_taken.append(c)
        else:
            print(f"You won in {limit-attempt} attempts")
            break
    


def _doTheThing():
    global guesses_taken, secret, game_ended

    text = ''
    for letter in secret:
        if letter in guesses_taken:
            text += letter + " "
        else:
            text += "_ "
 
    if secret in guesses_taken or "_" not in text:
        game_ended = bool(True)
        return text
    else:
        return text

if __name__ == "__main__":
    play()
    
