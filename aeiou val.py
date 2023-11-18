v,c = 0,0
vowel = 'aeiouAEIOU'
S = 'LoginVELACHERY'
for val in S:
    if val in vowel:
        v+=1
    else:
        c+=100
print (v,c)