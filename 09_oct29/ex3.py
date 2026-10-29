def myfunc(x):
    print('перше x =', x)
    x = 24
    print('друге x =', x)

a = 12
print('a =', a)
myfunc(a)
print('фінальне a =', a)

###
print('-------------------------------------')

def myfunc(x):
    print('перше x =', x)
    x.append(24)
    print('друге x =', x)

a = [12, -12]
print('a =', a)
myfunc(a)
print('фінальне a =', a)
