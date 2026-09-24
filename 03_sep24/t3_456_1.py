n = 879123999999995

s = 0
for j in range(10):
    print(n, n % 10, n // 10)
    s = s + n % 10
    n = n // 10

print(s)