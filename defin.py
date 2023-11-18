def add(a,b):
    return(a+b)

def max(l):
    max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    return max

def update(l2):
    l2[0]=100
    return l2


var1=10
var2=15
print(add(var1,var2))
print(add(20,30))
print(max([1,2,3,4,5,66,4]))
l=[1,2,3,4,5,66,4]
print(update)
