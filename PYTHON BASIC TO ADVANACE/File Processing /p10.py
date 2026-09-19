# Binary File Processing

source_image = input("Enter Source Image Name: ")
destination_image = input("Enter new Image Name: ")

# read image in binary 

with open(source_image, "rb") as file:
	image_data = file.read()

# wirte image in binary 

with open(destination_image, "wb") as file:
	file.write(image_data)

print("Image Copied Successfully.")