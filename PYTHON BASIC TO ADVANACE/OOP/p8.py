# pass, continue, break

correct_username = "Dhaval"
correct_password = "1234"

while True:

	username = input("Enter username: ")
	password = input("Enter password: ")

	if username == "" or password == "":
		pass
		print("Username or Password Cannot be Empty")
		continue

	if username == correct_username and password == correct_password:
		print("Login Successful!")
		break

	else:
		print("Wrong Username and Password")
		continue