n = int(input("user input : "))
sum = 0
#rem=n%10 to get last element from n
#n=n//10 eliminate last element from n
while (n>0):
    rem = n%10
    sum = sum+rem
    n = n//10
print(sum)