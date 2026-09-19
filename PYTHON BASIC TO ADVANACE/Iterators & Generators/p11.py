# Memory & Performance Benefits

import sys

data = input("Enter numbers separated by space: ")

numbers = list(map(int, data.split()))

list_square = [x * x for x in numbers]

genrator_square = [x * x for x in numbers]

print("\nList Result: ")
print(list_square)

print("\nGenerator Result: ")
for value in genrator_square:
	print(value)

print("\nMemory Usage: ")
print("List: ", sys.getsizeof(list_square), "bytes")
print("Generator: ", sys.getsizeof(genrator_square), "bytes")