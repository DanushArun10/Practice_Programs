# try:
#     a = int(input('enter A value : '))
#     b = int(input('enter B value : '))
#     c = a/b
#     print(c)
# except Exception as e:
#     print('enter a valid type')

#   this is used to handle errors when they occur
try:
    a = int(input('Enter A value : '))
    b = int(input('Enter B value ; '))
    print(a/b)
    # print(c) is a name error
except ZeroDivisionError:
    print('you cant div by 0')
except ValueError:
    print('Please enter a valid value')
except:
    print('error')
# else:
#   print('executed successfully') it was executed when there is no error
# finally:
#   print('good') it is used when error occur or not