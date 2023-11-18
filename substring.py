# n = input('enter a string : ')
# m = input('sub string : ')
# if m not in n:
#     print('not a substring')
# else:
#     print('substring')
#
#
#
# def substring (string1, string2):
#         if string1 in string2:
#             return string1
#         else:
#             return string2
#
#
# string1 = input('Enter a string : ')
# string2 = input('Enter a sub string : ')
# if string2 in string1:
#     print('It is a substring')
# else:
#     print('Not a substring')

a = input('Enter a string : ') #login360
b = input('Enter a sub string : ') #360
c = b[0] #3
count = 0
flag = 0
for i in range(len(a)):
    if a[i] == c:
        j = i
        for k in range(len(b)):
            if b[k]==a[j] and j<len(a)-1:
                count+=1
                j+=1
    if count == len(b):
        flag = 1
        print ('ksksk....')
    count = 0

if flag == 1:
    print('it is a substring')
else:
    print('not a substring')

