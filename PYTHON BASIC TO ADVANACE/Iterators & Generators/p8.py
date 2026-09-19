# Infinite Generators

terms = int(input("How many Fibonacci numbers print? "))

def fibonacci():

	a, b = 0, 1

	while True:
		yield a
		a, b = b, a + b

fib = fibonacci()

for i in range(terms):
	print(next(fib))