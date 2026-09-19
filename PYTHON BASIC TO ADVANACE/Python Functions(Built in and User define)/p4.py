# index() and count()

items = []

n = int(input("Enter number of items: "))

for i in range(n):
	item = input(f"Enter item {i+1}: ")
	items.append(item)

# index()

search_item = input("\nEnter item to find index: ")

print("Index:", items.index(search_item))

print("######################")

# count()

count_item = input("Enter item to count: ")

print("Count:", items.count(count_item))