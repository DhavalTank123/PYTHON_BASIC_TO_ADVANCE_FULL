# Exception Handling Decorators

def exception_handler(func):

	def wrapper(*args, **kwargs):

		try:
			return func(*args, **kwargs)

		except ZeroDivisionError:
			print("Cannot divide by zero")

		except ValueError:
			print("Please enter only numbers")

		except Exception as error:
			print("Unknown Error:", error)

	return wrapper

@exception_handler
def divide(num1, num2):

	print("Answer:", num1 / num2)


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

divide(num1, num2)