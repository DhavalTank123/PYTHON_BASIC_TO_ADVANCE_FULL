# yield from Statement

def user_numbers(numbers):

	yield from numbers

data = input("Enter numbers: ")

numbers = list(map(int, data.split()))

for n in user_numbers(numbers):
	print(n)