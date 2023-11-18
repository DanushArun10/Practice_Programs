def add(a,b,c):
    return a+b+c
l1 = [1,2,3,4,5]
l2 = [9,8,7,6,9]
l3 = [5,6,7,8]

m = map(add,l1,l2,l3)
n = map(max,l1,l2,l3)
print(tuple(m))
print(list(n))