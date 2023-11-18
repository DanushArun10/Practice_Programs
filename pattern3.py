n = 4
s = n-1
for i in range(n*2-1):
    for j in range(n):
        if j>=s:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    if i<n-1:
        s-=1
    else:
        s+=1
    print('')