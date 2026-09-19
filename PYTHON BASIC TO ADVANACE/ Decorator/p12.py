# Class-Based Decorators

class Welcome:

	def __init__(self, func):
		self.func = func

	def __call__(self):

		print("Welcome User")

		self.func()

		print("Thank You")

@Welcome
def greet():

	name = input("Enter Your Name: ")

	print("Hello", name)

greet()