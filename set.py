s = set()
s.add (1)
s.update("string", "tuple")
print(s)
s.remove('g')
print (s)
s.pop()
print (s)

a = set('bharath')
b = set('dhanush')
#a.intersection(b)
#print (a)
#a.symmetric_difference(b)
#print (a)
a.pop()
print (a)