d = {'name':'sam', 'role':'HR', 'company':'google'}
print(d['name'])
print(d['role'])

c = {1:'this', 2:'has', 3:'his', 1.0:'her', True:'their', 3:'three', 3.0:'false', 4:'float', 4.0:'floor'}
print(c[2])
print(c[1])
print(c[3])
print(c[4])

a = {'odd':[1,2,3,4], 'even':(2,3,4,5), 'prime':{3,4,5,6}}
print(a['odd'])
print(a['even'])
print(a.get('prime'))

b = {'odd':[1,3,5,7], 'even':(2,4,6,8), 'prime':{2,3,5,7}}
print(b['odd'])
print(b.keys())
print(b.values())
print(b.items())

d = {}
d['odd'] = [1,2,3,4]
print(d)
d['odd'] = 3
print(d)

for keys in b.keys():
    print(keys)

for values in b.values():
    print(values)

for keys,values in b.items():
    print(keys,values)
