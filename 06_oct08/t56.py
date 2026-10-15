
#n = 6755343
#n = 777
n = 314313

n_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#          0  1  2  3  4  5  6  7  8  9
n_times = [0] * 10 # альтернатива

while n > 0:
    digit = n % 10
    print(digit)
    n_times[digit] = n_times[digit] + 1

    n = n // 10

print(n_times)