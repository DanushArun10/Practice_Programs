n = int(input("Enter a N Number: "))
l = []
for a in range(2,n):
        for b in range(2,a):
            if(a%b)==0:
                break
        else:
            print(a)