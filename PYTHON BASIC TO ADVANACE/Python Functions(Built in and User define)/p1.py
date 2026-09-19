# append() and extend()

students = []
students1 = []

n1 = int(input("Enter number of students in first list: "))

for i in range(n1):
    name = input(f"Enter student {i+1}: ")
    students.append(name)

n2 = int(input("\nEnter number of students in second list: "))

for i in range(n2):
    name = input(f"Enter student {i+1}: ")
    students1.append(name)

new_student = input("\nEnter a student to append: ")
students.append(new_student)

print("\nAppend:", students)

print("########################")

students.extend(students1)

print("Extend:", students)
