a1 = int(input("Enter the Row for : "))
b1 = int(input("Enter the col for : "))
m = []
n = []
for i in range(a1):
    l = [int(i) for i in input().split()]
    m.append(l)
print(m)
for i in range(b1):
    l = [int(i) for i in input().split()]
    n.append(l)
print(n)
m1 = []
if len(m[0])==len(n):
    for i in range(len(m)):
        m1.append([])
        for j in range(len(m[0])):
            sum = 0
            for k in range(len(n)):
                sum += m[k][i]*n[k][j]
            m1[i].append(sum)
print(m1)

