from random import randint
class Dice:
    def __init__(self, num_sides:int) -> None:
        self.num_sides = num_sides

    def roll(self) -> int: 
        return (randint(1,self.num_sides))