b =1000014
if b % 2 == 0:
    print (b,'even')
else :
    print (b,'odd')

# max

l = [2,4,56,8,5,4]
maxi = l [0]
for i in range (len(l)):
    if l[i]>maxi:
        maxi = l[i]
print (maxi)

# fac

n=5
fact = 1
for i in range (1,n+1):
    fact = fact*i
print (fact)

l=[2,4,56,8,5,4]
sum = 0
for i in range(len(l)):
    sum = sum+l[i]
print (sum)