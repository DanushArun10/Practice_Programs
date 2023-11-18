def min(l):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min


def max(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max





l = [2,5,8,4,9,3,56]
print(min(l))
print(max(l))