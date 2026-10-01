cnt = 0

for k in range(10, 99+1):
    a = k // 10
    b = k % 10
    if a%2 == b%2:
        cnt = cnt + 1
        print(k, a, b, '<--це число нам підходить')

print(cnt)