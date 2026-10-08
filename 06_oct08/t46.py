n = 49 # int(input())

# 2....n-1

# is_prime = True
# j = 2
# while is_prime and j < n:
#     if n % j == 0:
#         print(f'{n} ділиться на {j}')
#         is_prime = False
#     j = j + 1


is_prime = True

for j in range(2, int(n**0.5) + 1):
    if n % j == 0:
        print(f'{n} ділиться на {j}')
        is_prime = False
        break

print('Чи є число простим?', is_prime)
