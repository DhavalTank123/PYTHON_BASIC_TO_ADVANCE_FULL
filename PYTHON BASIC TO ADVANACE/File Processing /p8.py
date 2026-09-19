#  INI/Configuration File Processing  

import configparser

app_name = input("Enter Application Name: ")
version = input("Enter version: ")
username = input("Enter Username: ")

config = configparser.ConfigParser()

config["Application"] = {
	"name": app_name,
	"version": version,
	'username': username
}

with open("settings.ini", "w") as file:
	config.write(file)

print("Configuration saved Successfully.")