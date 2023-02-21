class user:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = user("1", "rohit")
user2 = user("2", "me")

user1.follow(user2)
print(user1.following)


import requests
