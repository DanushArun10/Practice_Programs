# join method
T = ['jhon','peter','vicky']
s = ''
sep = '.'
for i in range(len(T)):
    if len(T)-1==i:         #logic method
        s+=T[i]
    else:
        s+=T[i]+sep
print(s)

s2 = '.'.join(T)            #string method
print(s2)



t = ['john','peter','vicky']
s1 = ''
sep1 = '/'
for i in range(len(t)):         #logic method
    s1+=t[i]+sep1
s1 = s1[:len(s1)-1]
print(s1)

s3 = '/'.join(t)                #string method
print(s3)

# count method
def count(s,string):
    c = 0
    for letter in s:            #using logic
        if letter == string:
            c+=1
    return c



s = 'login360vloging'
print(s.count('o'))

print(count(s,'g'))             #string method


class str:
    def _init_(self,s1):
        self.s1 = s1
    def count(self,string):
        c = 0
        for letter in self.s1:       #count function by logic
            if letter == string:
                c += 1
        return c


s1 = input("enter a string for S1 : ")
s2 = input("enter a string for S2 : ")
print(s.count('o'))
print(s2.count('l'))


print(count(s,'g'))                 #inbuilt function



'ascii value'
# 32 space
# 65 Upper case A
# 66 Upper case B.....
# 97 Lower case a
# 98 Lower case b.....