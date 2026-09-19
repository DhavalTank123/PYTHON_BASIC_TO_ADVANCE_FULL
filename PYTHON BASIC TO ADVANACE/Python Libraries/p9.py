# Logging

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin":
    logging.info("Admin login successful")
    print("Login Success")
else:
    logging.error("Login failed for user: " + username)
    print("Invalid Login")
