"""Project: Quiz Game
Start: February 17th, 2024
Last touched: February 17th, 2024
Author: Madeleine L.
"""

class User:
    # pass  # If you want to have an empty function or class use pass
    # constructor (or initialize) we use a special function __init__. This will be called every time we create a new
    # object from class
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# create object from class with attribute as arguments
user_1 = User("001", "mimi")
user_2 = User("002", "buck")

print(user_2.followers)
user_1.follow(user_2)
print(user_2.followers)

