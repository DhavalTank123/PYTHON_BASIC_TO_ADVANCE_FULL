# Timing & Performance Decorators

import time 

def timer(func):

	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()

		execution_time = end_time - start_time

		print("LOG: Funcation Name: ", func.__name__)
		print("LOG: Execution Time: ", execution_time, "seconds")

		return result

	return wrapper

@timer
def calculate_product(num1, num2):

	result = num1 * num2

	print("Result: ", result)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

calculate_product(num1, num2)