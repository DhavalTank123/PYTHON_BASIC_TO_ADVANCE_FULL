# Method Overriding

class Student:

	def result(self):
		print("Student has a result")

class ScienceStudent(Student):

	def result(self):
		marks = int(input("Enter Science Marks: "))

		if marks >= 40:
			print("Science Student: Pass")
		else:
			print("Science Student: Fail")

class CommerceStudent(Student):

	def result(self):
		marks = int(input("Enter Commerce Marks: "))

		if marks >= 40:
			print("Commerce Student: Pass")
		else:
			print("Commerce Student: Fail")

choice = input("Enter Stream (Science/Commerce): ")

if choice == "Science":
	s = ScienceStudent()
elif choice == "Commerce":
	s = CommerceStudent()
else:
	s = Student()

s.result()