#prime:
p = []
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
         p.append(j)
print('p')


#mul of the element:
n = input('enter a elements : ')
mul = 0
for i in range(len(n)):
    mul*int(len(n))
print(mul)

#gcd
n1 = int(input('enter n1 : '))
n2 = int(input('enter n2 : '))
if n1>n2:
    n1,n2 = n2,n1
gcd = 1
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        gcd = i
print(gcd)

# #special char
# s = input('enter a string : ')
# s1 = []
# ch = '.,!-'
# n = 0
# q = 0
# for i in range (len(s)):
#     if ch in str:
#         n = n + 1
#     else:
#         q = q + 1
# print(n)

w = [1,2,4,2,4]
b = 1
for i in range(w):
    b = b*i
print(b)