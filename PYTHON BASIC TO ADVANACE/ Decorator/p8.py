# Caching Decorators 

from functools import lru_cache

@lru_cache(maxsize=5)
def square(n):
	print("Calculating....")
	return n * n 

while True:
	number = int(input("Enter a number (-1 to exit): "))

	if number == -1:
		break

	result = square(number)
	print("Square = ", result)