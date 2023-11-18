def check(n):
    if n%2==0:
        return n,"It is even number"
    else:
        return n,"It is odd number"
#a=int(input("Enter a number: "))
#print(check(a))

l=[1,2,4,3,5,4]
for i in range(len(l)):
    print(check(l[i]))

