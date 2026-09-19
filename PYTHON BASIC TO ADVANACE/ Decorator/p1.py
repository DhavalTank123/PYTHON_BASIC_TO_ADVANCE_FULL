# Custom Decorators and Authentication

def password_required(func):

    def wrapper(*args, **kwargs):
        password = input("Enter Password: ")

        if password == "12345":
            return func(*args, **kwargs)

        else:
            print("Wrong Password")

    return wrapper


@password_required
def dashboard():
    print("Welcome dashboard!")


@password_required
def user_profile(name, age):
    print("Name:", name)
    print("Age:", age)


@password_required
def account_details(username, status="Active"):
    print("Username:", username)
    print("Status:", status)


# Function calls

dashboard()

user_profile("Rahul", 25)

account_details(username="Amit", status="Blocked")