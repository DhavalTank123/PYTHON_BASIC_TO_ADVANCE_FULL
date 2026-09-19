# sort() and reverse()

numbers = []

n = int(input("Enter number of element: "))

for i in range(n):
	num = int(input("Enter number {i+1}: "))
	numbers.append(num)

# sort()

numbers.sort()

print("Sort: ", numbers)

print("#################")

#reverse()

numbers.reverse()

print("Reverse: ", numbers)