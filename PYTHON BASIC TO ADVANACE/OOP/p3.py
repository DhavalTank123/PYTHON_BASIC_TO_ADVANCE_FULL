# Mixins 

class LoggerMixin:

	def log(self, message):
		print("LOG: ", message)

class Student(LoggerMixin):

	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def show(self):
		self.log("Student Details Displayed")
		print("Name: ", self.name)
		print("Marks: ", self.marks)

name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))

s = Student(name, marks)
s.show()