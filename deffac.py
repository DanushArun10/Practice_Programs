#Recursion
def fact(n):
    if n<=1:    #base condition
        return n
    else:   # recursive condition
        return n * fact(n-1)


print(fact(5))
