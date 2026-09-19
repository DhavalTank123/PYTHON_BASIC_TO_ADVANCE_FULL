#  os

import os

print("----- Employee Report System -----")

employee_name = input("Enter employee name: ")
salary = input("Enter employee salary: ")

folder = "Employee_Reports"

# Check folder exists
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Report folder created ")
else:
    print("Report folder already exists ")


# Create employee report file
file_path = os.path.join(
    folder,
    employee_name + ".txt"
)


with open(file_path, "w") as file:
    file.write("Employee Name: " + employee_name + "\n")
    file.write("Salary: " + salary + "\n")


print("Report generated successfully ")


# Show all reports
print("\nAvailable Reports:")

files = os.listdir(folder)

for file in files:
    print(file)
