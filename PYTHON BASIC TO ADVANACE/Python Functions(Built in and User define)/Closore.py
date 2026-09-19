# Closure 1

# def multiplier():

# 	x = int(input("Enter Multiplier Value: "))

# 	def multiply(y):

# 		return x * y

# 	return multiply

# multi = multiplier()

# num = int(input("Enter number to multiply: "))

# print("Result: ", multi(num))


# Closure 2 

def greeting():

	name = input("Enter Your Name: ")

	def message():
		print("Hello", name)

	return message

welcome = greeting()
welcome()
