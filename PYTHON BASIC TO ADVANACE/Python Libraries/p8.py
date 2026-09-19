import re

print("----- User Registration -----")

name = input("Enter your name: ")
mobile = input("Enter your mobile number: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Name validation
name_pattern = r"^[A-Za-z ]+$"

# Mobile validation
mobile_pattern = r"^[0-9]{10}$"

# Email validation
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Password validation
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$"


if re.match(name_pattern, name):
    print("Name is valid ")
else:
    print("Invalid name ")


if re.match(mobile_pattern, mobile):
    print("Mobile number is valid ")
else:
    print("Invalid mobile number ")


if re.match(email_pattern, email):
    print("Email is valid ")
else:
    print("Invalid email ")


if re.match(password_pattern, password):
    print("Password is strong ")
else:
    print("Password must contain:")
    print("- Minimum 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
