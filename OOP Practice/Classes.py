class Dog:
    def __init__(self, name, age):
        self.name:str = name
        self.age:int = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f'{self.age} rolled over!')

baby = Dog('Milo', 11)

print(f'look at {baby.name}! She is so cute!!!')
baby.sit()


