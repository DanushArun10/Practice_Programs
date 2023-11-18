l = [6,3,7,4,5,1,2]
n = len(l)
for index in range(n-1):
    m = index #m min index
    for i in range(index+1,n):
        if l[i]<l[m]:
            m = i
    (l[index],l[m]) = (l[m],l[index])
    print(l)