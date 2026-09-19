# Iterators & Generators

n = int(input("Enter how many number: "))

print("\nUsing Iterator: ")

iterator = iter(range(1, n + 1))

while True:
	try:
		print(next(iterator))
	except StopIteration:
		break

# Generators

def square_generator(limit):
	for i in range(1, limit + 1):
		yield i * i 

print("\nUsing Generator (Squares): ")

for square in square_generator(n):
	print(square)

