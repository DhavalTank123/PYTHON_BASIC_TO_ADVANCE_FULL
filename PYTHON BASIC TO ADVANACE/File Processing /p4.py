# JSON Import & Export

import json 

name = input("Enter Student Name: ")
age = int(input("Enter Student Ae: "))
city = input("Enter Student City: ")

student = {
	"name": name,
	"age": age,
	"city": city
}

with open("student.json", "w") as file:
	json.dump(student, file, indent=4)

print("Data Saved Successfully!")

with open("student.json", "r") as file:
	data = json.load(file)

print("\nStudent Details: ")
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])