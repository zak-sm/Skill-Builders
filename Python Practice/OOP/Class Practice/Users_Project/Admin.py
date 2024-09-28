from users_class import User
class Admin(User):
    def __init__(self, first_name: str, last_name, city: str, sex: str):
        super().__init__(first_name, last_name, city, sex)

        self.privilages = Privilages()



class Privilages():
    def __init__(self):

        self.privilages = ['Create User', 'Delete User', 'Reset Password','Disable Account']

    def show_privilages(self):
       
        print(f'Administrator Privilages: {self.privilages}')



