# Знайти кількість простих чисел, які не перевищують задане u
# Вказівка: створити список таких простих чисел

u = 200

primes = []

for n in range(2, u+1):
    print('------------------------------------------------')

    is_prime = True
    print(f'Ми хочемо перевірити, чи {n} -- просте')
    print('На цей момент нам відомі прості числа:', primes)
    for j in primes:
        if j > n**0.5:
            break
        if n % j == 0:
            print(f'{n} ділиться на {j}')
            is_prime = False
            break

    print(f'Чи є число {n} простим?', is_prime)
    if is_prime:
        primes.append(n)
        print('поточний список', primes)

print(f'Загалом ми знайшли {len(primes)} простих чисел')
print('Знайдені прості числа', primes)
