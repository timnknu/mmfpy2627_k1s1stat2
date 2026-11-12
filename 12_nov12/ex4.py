

def f(n):
    global abcd
    abcd = 12
    print('>>', abcd)
    return n**2

print(f(5))
print(abcd)
