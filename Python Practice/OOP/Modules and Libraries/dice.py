from random import randint
class Die():
    def __init__(self, sides):
        self.sides:int = sides

    def roll_die(self):
        
        print(f'Out of {self.sides} sides, you rolled a {randint(1,(self.sides))}')


sixdice = Die(6)
tendice = Die(10)
twentydice = Die(20)

sixdice.roll_die()
tendice.roll_die()
twentydice.roll_die()
