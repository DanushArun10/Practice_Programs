# n = 5
# for i in range(n):
#     for j in range(n):
#         print('* ', end = ' ')
#     print('')

n = 4
s = 0
for i in range(n):
    for j in range(n):
        if j>=s:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print(' ')
    s-=1
