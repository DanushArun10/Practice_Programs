m = [[5,0,0],[0,5,0],[0,0,5]]
c = m[0][0]
flag = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if i == j:
            if m[i][j] != c:
                flag = 1
                break
        else:
            if m[i][j] != 0:
                flag = 1
                break
if flag == 0:
    print('it is identical')
else:
    print('it is not identical')
