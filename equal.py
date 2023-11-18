flag=0
user = int(input())
for i in user:
    if i == "(" or i == "{" or i == "[":
        brak = brak+1
    if i== ")" or i == "}" or i == "]":
        brak -=1
    if brak<0:
        flag=1
        break
if brak==0 and flag==0:
    print("it is equal")
else:
    print("It is not equal")


