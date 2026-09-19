# copy() and len()

numbers = []

n = int(input("Enter number of element: "))

for i in range(n):
	num = int(input("Enter number {i+1}: "))
	numbers.append(num)

print("\nOriginal List: ", numbers)

# copy()

new_list = numbers.copy()
print("Copy List: ", new_list)

print("#########################")

# len()

length = len(numbers)
print("Length: ", length)