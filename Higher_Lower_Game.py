#Higher or Lower Game
import random

def HigherOrLower():
    answer:int = random.randint(1,500)
    correct:bool = False
    while correct == False:
        userguess:int = int(input('Guess the number between 1 and 100: '))
        if userguess > answer:
            print('Lower')
        elif userguess < answer:
            print('Higher!')
        elif userguess == answer:
            print(f'You guessed the correct number: {answer}')
            correct = True
HigherOrLower()