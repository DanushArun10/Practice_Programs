n = int(input("n : "))
l = []
l2 = []
for i in range(n):
    value = int(input())
    l.append(value)
print(l)
m = int(input("m : "))
for i in range(m):
    value = int(input())
    l2.append(value)
print(l2)
min_len = min(n, m)
l3 = []
for i in range(min_len):
    l3.append(l[i]+l2[i])
if m > n:
    l3 = l3+l2[n:]
else:
    l3 = l3+l[m:]
print(l3)