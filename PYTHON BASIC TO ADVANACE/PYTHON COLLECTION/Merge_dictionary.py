dict1 = {}

n = int(input("How Many Values in Dict: "))

for i in range(n):
	key = input("Enter The Name: ")
	Value = input("Enter The Value: ")

	dict1[key] = Value

dict2 = {
	"country": "India",
	"status": "Active"
}

dict1.update(dict2)
print(dict1)