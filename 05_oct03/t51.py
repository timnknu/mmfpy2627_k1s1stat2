lst = [1, -20, 50, 10000, -2, 11, 15, 1, 20000, -20, -20]
#      0   1    2    3     4   5   6  7    8     9    10   -- загалом 11 шт.
#lst = [-10, -2, -20, -20]

max_candidate = lst[0]
print(f'припустимо, що найбільший рівний {max_candidate}')

print(len(lst))
for i in range(1, len(lst)):
    print(i, '->', lst[i])
    if lst[i] > max_candidate:
        print(f' ми знайшли елемент {lst[i]} -- ще більший , ніж {max_candidate}')
        max_candidate = lst[i]
        print(f' отже, припустимо, що найбільший рівний {max_candidate}')

print('final:', max_candidate)

####

max_candidate = lst[0]
for a in lst:
    if a > max_candidate:
        max_candidate = a
print('final:', max_candidate)