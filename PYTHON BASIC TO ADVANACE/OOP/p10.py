# generators Funcation

def even_generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


num = int(input("Enter a number: "))

for value in even_generator(num):
    print(value)