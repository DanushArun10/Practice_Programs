l = ['cat','hat','tall','tap']
s1 = {'cat','hat','tall','tap'}
sum = set(l[0])
for i in range (len(l)):
    sum = sum & set(l[i])
print (sum)

s=set(s1.pop())
for item in s1:
    s = s&set(item)
print (s)

