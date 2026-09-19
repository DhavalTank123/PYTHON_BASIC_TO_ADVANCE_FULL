l = [
    [1,2,3,[4,5,[6,7]]]
]

def Flatten(l):
    res = []
    for i in l:
        if isinstance(i,list):
            res.extend(Flatten(i))
        else:
            res.append(i)
    return res

print(Flatten(l))