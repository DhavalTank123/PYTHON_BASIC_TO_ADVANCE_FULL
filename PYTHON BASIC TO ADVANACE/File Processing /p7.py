# YAML Processing

import yaml

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
course = input("Enter Course: ")
city = input("Enter City: ")

student = {
	"name": name,
	"age": age,
	"course": course,
	"city": city
}
with open("student.yaml", "w") as file:
	yaml.dump(student, file)

print("Student data saved successfully.")



# Real Life Uses:

# Docker Compose files
# Kubernetes configuration
# Application settings
# CI/CD pipelines
# Project configuration
