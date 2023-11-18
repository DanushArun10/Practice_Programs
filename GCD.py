n1 = int(input('value1 : '))
n2 = int(input('value2 : '))
if n1>n2:
    (n1,n2)=(n2,n1)
gcd=1
for i in range (1,n1+1):
    if n1%i==0 and n2%i==0:
        gcd = i
print(gcd)



