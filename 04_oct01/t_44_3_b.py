cnt = 0

for a in range(1, 9+1):
    print(a)
    for b in range(0, 9 + 1):
        print('...', b)
        if a%2 == b%2:
            cnt = cnt + 1
            print(a, b, '<--це число нам підходить')

print(cnt)