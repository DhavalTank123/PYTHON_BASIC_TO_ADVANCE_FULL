# pop(), map() and clear()

numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# pop()
index = int(input("\nEnter index to pop: "))

removed = numbers.pop(index)

print("\nPOP:", removed)

print("########################")

# map()
double_numbers = list(map(lambda x: x * 2, numbers))

print("Map:", double_numbers)

print("########################")

# clear()
numbers.clear()

print("Clear:", numbers)