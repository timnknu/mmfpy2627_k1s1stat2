
stat = {}
# ключі -- аргументи, з якими будь-коли викликалася fib
# значення -- кількість разів, з якими fib викликалася з аргументом==ключу
fibcache = {0: 1, 1: 1}
# ключі -- аргументи, з якими будь-коли викликалася fib
# значення -- результат fib, який відповідає аргументу==ключу


def fib(n):
    if n in fibcache:
        return fibcache[n]
    stat[n] = stat.get(n, 0) + 1

    y = fib(n-2) + fib(n-1)
    if n not in fibcache:
        fibcache[n] = y
    return y

a = fib(330)
print(a)
print(stat)