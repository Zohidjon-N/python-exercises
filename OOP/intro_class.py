class User:
    def __init__(self, name, username, email):
        self.name =  name
        self.login = username
        self.email = email
    def get_info(self):
        return f"User: {self.login}\nName: {self.name}\nEmail: {self.email}"

user1= User('Zohidjon','nojdihoz','soosheyyov@gmail.com')
print(user1.get_info())

name = input("Your name>> ")
username = input('Your username>> ')
email = input('Your email>> ')

user2= User(name,username,email)

print(user2.get_info())