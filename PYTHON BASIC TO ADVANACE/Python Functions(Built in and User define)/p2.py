# insert() and remove()

colors = []

n = int(input("Enter number of colors: "))

for i in range(n):
    color = input(f"Enter color {i+1}: ")
    colors.append(color)

# Insert
index = int(input("\nEnter index to insert: "))
new_color = input("Enter new color: ")

colors.insert(index, new_color)

print("\nAfter Insert:", colors)

print("########################")

# Remove
remove_index = int(input("Enter index to remove: "))

colors.pop(remove_index)

print("After Remove:", colors)