n = 4
s = n-1
e = n-1
for i in range(n):
    for j in range(n*2-1):
        if j>=s and j<=e:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print('')
    s-=1
    e+=1


# n = 5
# s = n-1
# e = n-1
# for i in range(n*2-1):
#     for j in range(n*2-1):
#         if j>=s and j<=e:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print(' ')
#     if i<n-1:
#         s-= 1
#         e+= 1
#     else:
#         s+= 1
#         e-= 1

