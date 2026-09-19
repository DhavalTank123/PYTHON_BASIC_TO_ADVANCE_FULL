# abs() and sorted()

numbers = []

n = int(input("Enter number of element: "))

for i in range(n):
	num = int(input("Enter number {i+1}: "))
	numbers.append(num)

# abs()

number = int(input("Enter number to find absolute value: "))
print("Absolute Value: ", abs(number))

print("#########################")

# sorted()

sorted_list = sorted(numbers)

print("Sorted List: ", sorted_list)

print("#########################")

# reversed()

reverse_list = list(reversed(numbers))

print("Reversed List: ", reverse_list)

