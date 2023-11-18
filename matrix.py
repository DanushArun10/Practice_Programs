r= int(input("Enter the Row: "))
m1=[]
m3=[]
for i in range(r):
    l=[int(i) for i in input().split()]
    m1.append(l)
print(m1)
m2=[]
for i in range(r):
    l = [int(i) for i in input().split()]
    m2.append(l)
print(m2)
j=len(m1[0])
if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            #print(m3)
            m3[i].append(m1[i][j]*m2[i][j])
    print(m3)
else:
    print('It is impossible to progress')
