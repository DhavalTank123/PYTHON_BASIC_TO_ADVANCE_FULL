# ZIP & Archive File Handling 

import zipfile
import os

file1 = input("Enter First file name: ")
file2 = input("Enter Second file name: ")

zip_name = input("Enter zip file name (example: backup.zip): ")

# Create zip 

with zipfile.ZipFile(zip_name, "w") as zip_file:
	zip_file.write(file1)
	zip_file.write(file2)


print("\nZip file Created Successfully")


# Unzip 

extract_folder = input("Enter folder name for extraction: ")

if not os.path.exists(extract_folder):
	os.mkdir(extract_folder)

# Extract

with zipfile.ZipFile(zip_name, "r") as zip_file:
	zip_file.extractall(extract_folder)

print("Zip Extracted Successfully")


print("\nExtracted Files: ")

for file in os.listdir(extract_folder):
	print(file)