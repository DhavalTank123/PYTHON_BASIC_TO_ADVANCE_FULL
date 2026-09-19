# Image File Processing

from PIL import Image 

image_name = input("Enter image file name: ")
new_image_name = input("Enter new image name: ")

width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

img = Image.open(image_name)

resized_img = img.resize((width, height))

resized_img.save(new_image_name)

print("\nImage resized successfully!")
print("New Size:", resized_img.size)