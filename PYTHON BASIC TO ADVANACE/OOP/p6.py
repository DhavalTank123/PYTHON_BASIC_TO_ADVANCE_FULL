# Property Method

class Employee:

    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self._salary = amount
        else:
            print("Salary cannot be negative")

e = Employee()

salary = int(input("Enter salary: "))

e.salary = salary

print("Employee Salary:", e.salary)

