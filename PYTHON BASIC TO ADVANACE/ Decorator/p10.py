# Transaction Decorators

def transaction(func):

	def wrapper(*args, **kwargs):

		print("Transaction Started")

		try:
			result = func(*args, **kwargs)
			print("Transaction Committed")
			return result

		except Exception as e:
			print("Transaction Rolled Back")
			print("Error:", e)

	return wrapper

@transaction
def withdraw(balance, amount):

	if amount > balance:
		raise Exception("Insufficient Balance")

	balance -= amount

	print("Withdrawal Successful")
	print("Remaining Balance: ", balance)

	return balance

balance = int(input("Enter The Your Balance: "))
print(balance)

amount = int(input("Enter Withdrawal amount: "))

withdraw(balance, amount)