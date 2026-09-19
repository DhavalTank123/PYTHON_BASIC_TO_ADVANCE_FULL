
l = [
    {
        'name': 'Alice', 
        'age': 25
    },
    {
        'name': 'Dhaval',
        'age': 30
    },
    {
        'name': 'Dhaval',
        'age': 30
    },
    {
        'name': 'Charlie', 
        'age': 22
    }
        
]


remove_duplicate = []
for i in l:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
print(remove_duplicate)

