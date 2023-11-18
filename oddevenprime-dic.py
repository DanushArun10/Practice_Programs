# d = {'odd':[], 'even':[], 'prime':[]}
# for i in range (1,101):
#     if i%2==0:
#         d['even'].append(i)
#     else:
#         d['odd'].append(i)
#     if i==1:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         d['prime'].append(i)
#
# print(d['odd'])
# print(d['even'])
# print(d['prime'])


np = []
p = []
for i in range(1,101):
    prime = 1
    for j in range(2,i):
        if i%j == 0:
            prime = 0
            break
    if prime == 1:
        p.append(i)
    else:
        np.append(i)

print(p,np)