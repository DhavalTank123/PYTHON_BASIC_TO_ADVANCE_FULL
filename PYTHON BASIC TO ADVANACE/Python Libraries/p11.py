# pathlib 

from pathlib import Path

print("---------------------")

photo_name = input("Enter photo name: ")

photo_folder = Path("My_Photos")

if not photo_folder.exists():
	photo_folder.mkdir()
	print("Photo folder created")
else:
	print("Photo folder already exists")

photo_file = photo_folder / (photo_name + ".jpg")

photo_file.touch()

print("photo saved successfully")

print("\nYour Photos: ")

for photo in photo_folder.iterdir():
	print(photo.name)