s = input("input : ")
b= 0
flag=0
for bracket in s:
    if bracket == "(":
        b += 1
    if bracket == "{":
        b += 1
    if bracket == "[":
        b += 1
    elif bracket == ")":
        b -= 1
    elif bracket == "}":
        b -= 1
    elif bracket == "]":
        b -= 1
    if b<0:
        flag=1
        break
if b==0:
    print("it is equal")
else:
    print("It is not equal")


