# Temporary File Handling

import tempfile

name = input("Enter your name: ")

with tempfile.TemporaryFile(mode='w+t') as temp:

	temp.write(name)

	temp.seek(0)

	print("Data stored in temporary file: ", temp.read())