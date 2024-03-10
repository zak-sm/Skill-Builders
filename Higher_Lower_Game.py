#Higher or Lower Game
import random
import os

def HigherOrLower():
    answer:int = random.randint(1,500)
    correct:bool = False
    count = 0

    while correct == False:
        try:
            count += 1
            userguess:int = int(input('Guess the number between 1 and 500: '))
            if userguess > answer and userguess <= 500:
                print('Lower')
            elif userguess < answer:
                print('Higher!')
            elif userguess == answer:
                correct = True
                print(f'You guessed the correct number: {answer}!!')
                print(f'It took you {count} guesses!')
                playAgain()
            elif userguess > 500:
                print('Whoops! Thats not a valid number, please try again.')
        except ValueError:
            print("That is not a valid entry")

            

def GameStart():
    playerResponse:str = str(input('''Thank you for playing Higher or Lower! \n
    Would you like to play? (Yes/No): '''))
    playerResponse = playerResponse[0]
    if 'y' in playerResponse:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Great!')
        HigherOrLower()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Okay, have a good day!")
        
 


def playAgain():
    playerResponse:str = str(input('Would you like to play again? (Yes/No): '))
    playerResponse = playerResponse[0]
    if 'y' in playerResponse:
        print('Awesome, here we go again!')
        HigherOrLower()
    else:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("Okay, have a good day. Thanks for playing!") 






GameStart()