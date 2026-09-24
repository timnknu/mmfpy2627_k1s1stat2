n = 87912387878785

s = 0
while n > 0:
    print(n, n % 10, n // 10)
    s = s + n % 10
    n = n // 10

print(s)