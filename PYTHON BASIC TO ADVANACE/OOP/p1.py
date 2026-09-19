# Single Inheritance 

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):

	def __init__ (self, name, age, course):
		super().__init__(name, age)
		self.course = course

	def display(self):

		print("\nStudent Details: ")
		print("Name: ", self.name)
		print("Age: ", self.age)
		print("Course: ", self.course)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

s = Student(name, age, course)
s.display()