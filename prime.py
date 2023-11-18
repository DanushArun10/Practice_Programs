n=int(input("Enter a N Number: "))
prime=1
for i in range(2,n):
    if n%i==0:
        prime=0
        break
if prime==1:
    print('prime')
else:
    print('Not a prime')
