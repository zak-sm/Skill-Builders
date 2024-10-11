class Restraurants:
    def __init__(self, restaurant_name:str, cuisine_type:str, number_served:int = 0):
        self.name:str = restaurant_name
        self.types:str = cuisine_type
        self.served:int = number_served


    def describe_restaurant(self):
        print(f'{self.name} is a restaurant that makes {self.types} food.')


    
    def open_restaurant(self):
        print(f'{self.name} is open for business!')

    def set_number_served(self, number_served):
        self.served = number_served
        return(self.served)

    def increment_number_served(self, incriment):
        self.served += incriment