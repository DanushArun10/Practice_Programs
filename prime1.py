num=int(input("Enter a number:"))
sum=0
count=0
for n in range(2,num):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
        sum+=n
        count+=1
print(sum)
print(count)