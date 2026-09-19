# Custom Iterators 

class CharacterIterator:

	def __init__(self, text):
		self.text = text
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.index < len(self.text):
			ch = self.text[self.index]
			self.index += 1
			return ch
		raise StopIteration

name = input("Enter your name: ")

char = CharacterIterator(name)

for letter in char:
	print(letter)