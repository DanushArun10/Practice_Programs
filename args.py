def fun(a,b,*args):
    sum=0
    for i  in range(len(args)):
        sum+=args[i]
    return sum
print(fun(5,3,4,6,7,8))