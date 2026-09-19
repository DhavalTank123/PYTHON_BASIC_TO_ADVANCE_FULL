# Singleton Decorator

def singleton(cls):

	instance = None

	def wrapper(*args, **kwargs):

		nonlocal instance

		if instance is None:
			instance = cls(*args, **kwargs)

		return instance

	return wrapper

@singleton
class User:

	def __init__(self, name):
		self.name = name

	def display(self):
		print("User Name: ", self.name)

name1 = input("Enter First User Name: ")
user1 = User(name1)

user1.display()

name2 = input("Enter Second User Name: ")
user2 = User(name2)

user2.display()

print("Are both objects same?", user1 is user2)