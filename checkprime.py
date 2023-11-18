def CheckPrime(n):
    prime=1
    for i in range(2,n):
        if n % i ==0:
            return 0
    return 1
#for n in range(1,101):
n = int(input("enter a number : "))
if CheckPrime(n):
    print(n,"prime")
else:
    print(n,"not prime")