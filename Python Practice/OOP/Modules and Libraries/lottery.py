from random import choice

class Lottery():
    def __init__(self) -> None:
        self.code = ['G',89, 14, 'L', 21, 69, 'R', 3, 94, 37, 'P', 18, 48, 11, 'C']
        self.numbers = []

    def get_numbers(self) -> list:
        cnumbers = []
        for i in range(4): cnumbers.append(choice(self.code))

        
        self.numbers = cnumbers

class Me():
    def __init__(self):
        self.my_numbers = ['G',89, 14, 'L', 21, 69, 'R', 3, 94, 37, 'P', 18, 48, 11, 'C']
        self.final_ticket = []
    def get_my_nums(self) -> list:
        my_ticket = []
        for i in range(4): 
            my_ticket.append(choice(self.my_numbers))
            self.final_ticket = my_ticket





ticket = Lottery()
ticket.get_numbers()

my_tic = Me()
my_tic.get_my_nums()


def analysis():
    count = 0 
    while ticket.numbers != my_tic.final_ticket:
        count += 1
        ticket.get_numbers()
        my_tic.get_my_nums()
        print(f'Attempt: {count}')
    print(f'''\n YOU WON THE LOTTERY!! \n It took you {count} tries to guess the right numbers. 
    Your Numbers: {my_tic.final_ticket} \n Winning Numbers: {ticket.numbers} \n''')

analysis()