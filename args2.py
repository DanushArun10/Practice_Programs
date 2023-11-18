def fun(a,b,c,*args):
    print(a,b,c)
    return args
#print(fun('sam','687867589',104,234,454,554))

def fun2(**kwargs):
    return kwargs

#a=fun2(first='login', sec='360', third=5)
#print(a)


def fun2(cus_name,no,*args,**kwargs):
    #print(cus_name,no)
    return args,kwargs,cus_name,no

a,b,c,d=fun2('sam','43245',3,'afeeg',4,milk='aavin',biscut='goodday')
print(a)
print(b)
print(c)
print(d)
