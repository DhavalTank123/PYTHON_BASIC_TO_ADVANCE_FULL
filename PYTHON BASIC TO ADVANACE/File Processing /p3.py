# CSV Import & Export 

import csv

# Export 

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
city = input("Enter Student City: ")

file = open("student.csv", "a", newline="")

writer = csv.writer(file) 
writer.writerow([name, age, city])

file.close()
print("/nData Exported Successfully.")

# Import

file = open("student.csv", "r")

render = csv.reader(file)

print("\nCSV File Content:")

for row in render:
	print(row)

file.close()
