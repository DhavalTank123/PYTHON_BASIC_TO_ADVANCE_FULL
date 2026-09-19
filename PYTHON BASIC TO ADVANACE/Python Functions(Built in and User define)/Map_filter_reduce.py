from functools import reduce

from functools import reduce
l = [5,10,15,20]
c=lambda x:x**3
c_l = []
for i in l:
    c_l.append(c(i))
print(c_l)


print(list(filter(lambda x:x%10==0,l)))

print(list(map(lambda x:x+5,l)))
print(reduce(lambda x,y:x+y,l))