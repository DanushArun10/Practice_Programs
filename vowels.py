# to fine vowels and consonent count

s = 'LoginVeLachery'
vowel = 'aeiouAEIOU'
v,c = 0,0
for i in range(len(s)):
    if s[i] in vowel:
        v+=1
    else:
        c+=1
print(v,c)