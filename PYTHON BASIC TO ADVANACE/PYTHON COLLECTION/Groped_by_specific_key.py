from collections import defaultdict


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

grouped_data = {}

for person in l:
    group_key = person["age"]
    if group_key not in grouped_data:
        grouped_data[group_key] = []
    grouped_data[group_key].append(person)

print(grouped_data)



# grouped_data = defaultdict(list)

# for item in l:
#     # Use the 'role' value as the grouping key
#     grouped_data[item["age"]].append(item)

# # Convert back to a standard dict if needed
# print(dict(grouped_data))
        
