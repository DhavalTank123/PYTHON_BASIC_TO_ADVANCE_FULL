# Multiple Inheritance 

class PersonalInfo:

	def __init__(self, name, age, **kwargs):
		super().__init__(**kwargs)
		self.name = name
		self.age = age

class EducationInfo:

	def __init__(self, course, collage, **kwargs):
		super().__init__(**kwargs)
		self.course = course
		self.collage = collage

class Student(PersonalInfo, EducationInfo):

	def __init__(self, name, age, course, collage):
		super().__init__(
			name=name,
			age=age,
			course=course,
			collage=collage
		)

	def display(self):
		print("\n----- Student Details -----")
		print("Name: ", self.name)
		print("Age: ", self.age)
		print("Course: ", self.course)
		print("Collage: ", self.collage)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
collage = input("Enter Colage: ")

s = Student(name, age, course, collage)
s.display()