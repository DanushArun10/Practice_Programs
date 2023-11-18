s=input()
count=0
for char in s:
    if not char.isalnum():
        count+=1
print (count)