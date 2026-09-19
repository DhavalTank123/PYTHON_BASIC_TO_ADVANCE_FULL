#  Validation Decorators

def validate_user(func):

	def wrapper(name, age, email):

		if name == "":
			print("Name Cannot be empty")
			return

		if age < 18: 
			print("Age Must be 18 or above")
			return

		if "@" not in email or "." not in email:
			print("Invalid Email Format")
			return

		return func(name, age, email)

	return wrapper

@validate_user
def create_account(name, age, email):
	print("Account Created")
	print("Name: ",name)
	print("Age: ", age)
	print("Email: ", email)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")

create_account(name, age, email)