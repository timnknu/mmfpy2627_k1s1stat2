def is_prime_number(n):
    is_prime = True
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            is_prime = False
            break
    return is_prime

#####


n = 100
for num in range(n, 2*n+1):
    res = is_prime_number(num) and is_prime_number(num+2)
    if res:
        print(num, f'нам підходить, бо {num} і {num+2} обидва є простими')

