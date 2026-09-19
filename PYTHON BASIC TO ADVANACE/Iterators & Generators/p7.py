# Lazy Evaluation

limit = int(input("Enter limit: "))

even_numbers = (x for x in range(limit + 1) if x % 2 == 0)

print("Generator is ready")

for num in even_numbers:
	print(num)