lst = [1, -20, 50, 10000, -2, 11, 15, 1, 20000, -20, -20]
#      0   1    2    3     4   5   6  7    8     9    10   -- загалом 11 шт.

max_candidate = lst[0]
print(f'припустимо, що максимум {max_candidate}')
for a in lst[1:]:
    print(f'аналізуємо {a}')
    if a > max_candidate:
        max_candidate = a
print('final:', max_candidate)

print('>>>', lst[0:8])
# range(0, 8) -> 0, 1, 2, 3, 4, 5, 6, 7
print('>>>', lst[1:])
# range(1, len(lst)) -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print('>>>', lst[0:len(lst):3])
# range(0, len(lst), 3) -> 0, 3, 6, 9

print('>>>', lst[::3])
# range(0, len(lst), 3) -> 0, 3, 6, 9

print('>>>', lst[::-1])