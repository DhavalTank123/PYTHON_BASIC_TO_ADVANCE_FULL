# super 

class Person:

	def __init__(self, name):
		self.name = name 

	def display(self):
		print("Name: ", self.name)

class Student(Person):

	def __init__(self, name, course):
		super().__init__(name)
		self.course = course

	def show(self):
		super().display()
		print("Course:", self.course)

name = input("Enter Student Name: ")
course = input("Enter Course Name: ")

studet = Student(name, course)
studet.show()