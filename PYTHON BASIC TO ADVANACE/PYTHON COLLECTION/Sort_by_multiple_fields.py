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
        'name': 'Charlie', 
        'age': 22
    }    
]

sorted_l = sorted(l, key=lambda x: (x['name'], x['age']))# first name so age sort not work you can change and it work
print(sorted_l)