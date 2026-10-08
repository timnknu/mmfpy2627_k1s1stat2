# Знайти кількість простих чисел, які не перевищують задане u

u = 100

primes = []

for n in range(2, u+1):

    is_prime = True

    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            print(f'{n} ділиться на {j}')
            is_prime = False
            break

    print(f'Чи є число {n} простим?', is_prime)
    if is_prime:
        primes.append(n)

print(f'Загалом ми знайшли {len(primes)} простих чисел')
print('Знайдені прості числа', primes)
