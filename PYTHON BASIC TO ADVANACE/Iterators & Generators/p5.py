# Generator Functions (yield)

def generator_number(n):
	for i in range(1, n + 1):
		yield i

n = int(input("Enter Limit: "))

gen = generator_number(n)

for num in gen:
	print(num)