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

filter_list = [person for person in l if person["age"] < 30]
print(filter_list)

# filter_list =  list(filter(lambda u: u["age"]  < 30, l))
# print(filter_list)