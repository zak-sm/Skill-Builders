from users_class import User as usr
from Admin import Admin
user2 = Admin('Neveen', 'Abdalla', 'Royal Oak', 'Female')



user1 = usr('Zak', 'Smith', 'Grosse Pointe Farms', 'Male')

print(user1.attempts, 'attempts')

user1.describe_user()
user1.greet_user()

user2.privilages.show_privilages()
