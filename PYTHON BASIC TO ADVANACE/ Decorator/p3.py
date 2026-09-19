# Logging Decorators

def logger(func):

	def wrapper(*args, **kwargs):

		print("LOG: Calling Funcation", func.__name__)
		print("LOG: Arguments: ", args)

		result = func(*args, **kwargs)

		print("LOG: Funcation executed successfully")

		return result

	return wrapper

@logger
def calculate_total(price, quantity):
	total = price * quantity
	print("Total Price: ", total)

price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

calculate_total(price, quantity)