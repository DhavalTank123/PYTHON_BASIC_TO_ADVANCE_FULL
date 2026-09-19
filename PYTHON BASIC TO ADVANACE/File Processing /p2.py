# File & Directory Management (os, pathlib, shutil)

import os
from pathlib import Path 
import shutil

filename = input("Enter File Name (e.g. student.txt): ")

data = input("Enter Data to Write: ")

file = open(filename, "w")
file.write(data)
file.close()

print("File Created  Successfully.")

path = Path(filename)

if path.exists():
	print("File Exists")
	print("File Name: ", path.name)
	print("Extension: ", path.suffix)


file = open(filename, "r")
print("\nFile Content:")
print(file.read())
file.close()

copyname = input("\nEnter copy file name: ")
shutil.copy(filename, copyname)
print("File Copied Successfully.")

choice = input("Do you want to delete original file? (yes/no): ")

if choice == "yes":
	os.remove(filename)
	print("Original File Deleted.")

else: 
	print("File Note Deleted.")