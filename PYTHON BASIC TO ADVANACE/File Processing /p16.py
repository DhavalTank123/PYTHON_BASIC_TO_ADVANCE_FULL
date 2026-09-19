# File Validation & Error Handling

import os

filename = input("Enter file name: ")

try:

	if not os.path.exists(filename):
		raise FileNotFoundError("File does not exists")

	allowed_extensions = [".txt", ".py", ".csv"]

	extension = os.path.splitext(filename)[1]

	if extension not in allowed_extensions:
		print("Invalid file type")
	else:
		with open(filename, "r") as file:
			data = file.read()

		print("\nFile is valid")
		print("File Content")
		print(data)

except FileNotFoundError as e:
	print("Error:", e)

except PermissionError:
	print("Permission Denied")

except Exception as e: 
	print("Unexpected Error:", e)

