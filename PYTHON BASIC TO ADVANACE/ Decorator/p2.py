# Authorization & Permission Decorators

def permission_required(required_role):

	def decorator(func):
		def wrapper(username, role, *args, **kwargs):

			if role == required_role:
				return func(username, role, *args, **kwargs)

			else:
				print("Access Denied: You don't have permission")

		return wrapper

	return decorator

@permission_required("admin")
def delete_user(username, role):
	print(username, "deleted a user")

@permission_required("manager")
def approve_leave(username, role):
	print(username, "Upproved Leave")


username = input("Enter Username: ")
role = input("Enter Role (admin/user/manager): ")

delete_user(username, role)

approve_leave(username, role)