str='1235469780'
str2='676'
#print(str2)
sum=0
for i in range(len(str2)):
    sum += str.index(str2[i])
print(sum)
#print(str.index())