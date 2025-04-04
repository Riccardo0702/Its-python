class User:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        print(f"User's information: First name:{self.first_name}, Last name:{self.last_name}, Age:{self.age}, Height: {self.height}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}, nice to meet you!")


user1= User("Riccardo", "Paladini", 20, 1.75)
user2= User("Edoardo", "Valentini", 21, 1.78)
user3= User("Edoardo", "Levi", 20, 1.75)

user1.describe_user()
user2.describe_user()
user3.describe_user()
