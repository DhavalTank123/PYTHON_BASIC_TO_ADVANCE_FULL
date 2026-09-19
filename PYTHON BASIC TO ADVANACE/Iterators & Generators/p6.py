# Generator Expressions

numbers = input("Enter numbers separated by space: ")

numbers = map(int, numbers.split())

squares = (x * x for x in numbers)

for value in squares:
	print(value)