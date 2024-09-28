class User:
    def __init__(self, first_name:str, last_name, city:str, sex:str):
        self.first = first_name
        self.last = last_name
        self.full = first_name + ' ' + last_name
        self.city = city
        self.sex = sex
        self.attempts = 0 

    def describe_user(self):
        print(f''' \nUser  Details: \n Name: {self.first} {self.last} \n City of Residence: {self.city} \n Sex: {self.sex} \n ''')
        
    def greet_user(self):
        print(f'Hello {self.full}, Welcome. \n')

    def incriment_login_attempts(self):
        self.attempts += 1

    def reset_login_attempts(self):
        self.attempts = 0 

