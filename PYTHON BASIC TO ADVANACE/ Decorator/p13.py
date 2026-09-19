# Parameterized Decorators

def greeting(message):

	def decorator(func):

		def wrapper(name):

			print(message)

			func(name)

		return wrapper

	return decorator

@greeting("Welcome to Python")
def student(name):

	print("Student Name: ", name)

name = input("Enter your name: ")

student(name)