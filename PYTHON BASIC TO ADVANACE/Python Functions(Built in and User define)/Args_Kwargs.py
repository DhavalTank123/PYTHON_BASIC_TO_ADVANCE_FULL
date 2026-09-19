# *args and **kwargs with User Input 

def student_details (*marks, **details):

	print("\nStudent Marks: ")
	print(marks)

	total = sum(marks)

	print("Total Marks: ", total)

	print("\nStudent Information: ")
	for key, value in details.items():
		print(key, ":", value)


# User Input for *args

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
	mark = int(input(f"Enter subject {i+1} marks: "))
	marks.append(mark)


# User Input for **kwargs

name = input("\nEnter Student Name: ")
age = int(input("Enter Student Age: "))
course = input("Enter Course Name: ")


# Calling Function 

student_details(*marks, name=name, age=age, course=course)