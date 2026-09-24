n = 652
numd = 0
s = 0
p = 1
A = 0
while n > 0:
    digit = n % 10
    print(digit)
    s = s + digit
    p = p * digit
    numd = numd + 1
    n = n // 10
    A = A * 10 + digit

print(A)
print(s, numd, p)
print(p / s)