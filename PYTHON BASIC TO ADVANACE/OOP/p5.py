# Abstract Method

from abc import ABC, abstractmethod

class Shape(ABC):

	@abstractmethod
	def area(self):
		pass

class Circle(Shape):

	def area(self):
		r = int(input("Enter Radius: "))
		print("Circle Area: ", 3.14 * r * r)

class Square(Shape):

	def area(self):
		side = int(input("Enter Side: "))
		print("Square Area: ", side * side)

choice = input("Enter Shape (Circle/Square):")

if choice == "circle":
	s = Circle()
else:
	s = Square()

s.area()