# sum(), max() and min()

numbers = []

n = int(input("Enter number of element: "))

for i in range(n):
	num = int(input(f"Enter number {i+1}: "))
	numbers.append(num)

# sum()

total = sum(numbers)
print("Sum: ", total)

print("###################")

# max()

maximum = max(numbers)
print("Maximum: ", maximum)

print("########################")

# min()

minimum = min(numbers)
print("Minimum: ", minimum)