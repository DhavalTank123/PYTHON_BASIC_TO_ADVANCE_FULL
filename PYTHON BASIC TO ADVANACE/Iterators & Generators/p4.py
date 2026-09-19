# Built-in Iterarors Using Dictionary & Enumerate Iterator 

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
city = input("Enter Student City: ")


student = {
	"name": name,
	"age": age,
	"city": city
}

# Dictionary Iter

it = iter(student)

# Enumerate Iter

for index, key in enumerate(it):
	print(index, key, ":", student[key])
