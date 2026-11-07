def nsd(a, b): # GCD
    if b == 0:
        return a

    if a == 0:
        return b

    if a >= b:
        y = nsd(a % b, b)
        return y

    y = nsd(b % a, a)
    return y


#x = nsd(7*7*23, 5*7**2*11*19)
x = nsd(0, 7*7*23)
print(x)