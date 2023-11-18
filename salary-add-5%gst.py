s = int(input("Enter S.no : "))
x = []
sum = 0
for i in range(s):
    v = int(input())
    x.append(v)
for i in range(len(x)):
    if x[i]>10000:
        x[i]=x[i]-((x[i]/100)*5)
        sum += x[i]
        print(sum)

