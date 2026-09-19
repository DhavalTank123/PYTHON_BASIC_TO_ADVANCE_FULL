# Generator Methods (send(), throw(), close())

def calculator():

	total = 0

	try:
		while True:

			value = yield total 

			if value < 0:
				raise ValueError("Negative number not allowed")

			total += value 

	except ValueError as e:
		print("Error:", e)

	finally:
		print("Generator Closed")

gen = calculator()

print("Starting Total:", next(gen))

while True:

	user_input = input("Enter number (stop = close, error = throw): ")

	if user_input == "stop":
		gen.close()
		break

	elif user_input == "error":
		gen.throw(ValueError)
		
		break

	else:
		result = gen.send(int(user_input))
		print("Current Total: ", result)