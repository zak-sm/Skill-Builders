from Restaurant import Restraurants
class IceCreamStand(Restraurants):

    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)

        self.flavors:list = ['Chocolate', 'Vanilla', 'Oreo']

    def display_flavors(self):
        print(f'The following flavors are available at {self.name}! : \n {self.flavors}')


ashbys = IceCreamStand('Ashbys', 'Ice Cream', 781) 

hydrenga = Restraurants('Hydrenga Kitchen', 'Cafe')



hydrenga.set_number_served(42)
hydrenga.increment_number_served(18)
hydrenga.describe_restaurant()
hydrenga.open_restaurant()
print(hydrenga.name, hydrenga.types, hydrenga.served)
ashbys.display_flavors()