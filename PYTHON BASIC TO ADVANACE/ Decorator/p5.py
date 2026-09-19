# Retry Decorators

def retry(max_attempts):

	def decorator(func):

		def wrapper(*args, **kwargs):

			for attempt in range(1, max_attempts + 1):

				try: 
					password = input("Enter Password: ")

					return func(password, *args, **kwargs)

				except Exception as error: 
					print("Attempt", {attempt}, "Failed:", {error})

			print("All attempts failed. Access Denied.")

		return wrapper

	return decorator

@retry(3)
def login(password):

	if password != "12345":
		raise Exception("Wrong Password")

	print("Login Successful!")

# password = input("Enter Password: ")
# login(password)

login()