str = (input("enter a string : "))
s=0
e=len(str)-1
print(e)
palindrome = 1
while s>e:
    if str[s]!=str[e]:
        palindrome = 0
        break
    s += 1
    s -= 1
if palindrome == 0:
    print("not a  palindrome")
else:
    print("palindrome")