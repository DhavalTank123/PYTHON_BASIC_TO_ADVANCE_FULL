# Rate Limiting Decorators

import time

def rate_limit(max_calls, time_window):
	calls = []

	def decorator(func):

		def wrapper(*args, **kwargs):

			current_time = time.time()

			while calls and calls[0] < current_time - time_window:
				calls.pop(0)

			if len (calls) >= max_calls:
				return "Rate limit exceeded. Try again later."

			calls.append(current_time)

			return func(*args, **kwargs)

		return wrapper

	return decorator

@rate_limit(max_calls=3, time_window=10)
def send_message(message):
	return "Message sent: " + message

while True:

	user_input = input("Enter your message (type exit to stop): ")

	if user_input == "exit":
		break

	result = send_message(user_input)

	print(result)