n = 4
star = 1
space = 0
stars = 9
for i in range(n*2-1):
    print(''*space+'*'*star)
    space -= 1
    star += 1

for j in range(n*2+1):
    print('' * space + '*' * stars)
    space += 1
    stars -= 1