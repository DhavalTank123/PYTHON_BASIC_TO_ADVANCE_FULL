# Pickle Serialization

import pickle

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
course = input("Enter Course: ")

student = {
	"name": name,
	"age": age,
	"course": course
}
# Serialization

with open("student.pkl", "wb") as file:
	pickle.dump(student, file)

print("Student data saved!")

# DeSerialization

with open("student.pkl", "rb") as file:
	data = pickle.load(file)

print("\nStudent Details: ")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])