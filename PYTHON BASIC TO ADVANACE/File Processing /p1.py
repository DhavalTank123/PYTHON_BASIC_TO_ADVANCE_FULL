# File Processing 

# Reading & Writing Text Files (Using read(), open(), write(), append() operation)


name = input("Enter your name: ")

file = open("sample.txt", "w")
file.write(name)
file.close()

print("Data saved Successfully.")


file = open("sample.txt", "r")

print("\nFile Content:")
print(file.read())
file.close()

new_name = input("\nEnter another name: ")

file = open("sample.txt", "a")
file.write("\n" + new_name)
file.close()

print("\nData Appended Successfully.")

file = open("sample.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()