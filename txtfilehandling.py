file = open('defin.py','r')
''' s = file.read() #readlines used to make a single line list slipt based on \n, readline used to access line by line.
print(s)
file.close()
'''


string = file.readline()
while(string):
    print(string)
    string = file.readline()
file.close()