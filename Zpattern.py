n=int(input())
s=n-1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or s==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    s-=1