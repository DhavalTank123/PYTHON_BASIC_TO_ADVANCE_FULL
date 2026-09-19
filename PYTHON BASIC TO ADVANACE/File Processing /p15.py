# File Upload & Download

upload_file = input("Enter existing file name: ")

with open(upload_file, "r") as file:
    data = file.read()

print("\nCurrent Content:")
print(data)

# Edit
extra = input("\nEnter text to add: ")

updated_data = data + "\n" + extra

# Download (Save as new file)
download_file = input("\nEnter download file name: ")

with open(download_file, "w") as file:
    file.write(updated_data)

print("File downloaded successfully!")
