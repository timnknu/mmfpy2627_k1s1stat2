# 5.3. Номер на 3
# Задано послідовність дійсних чисел a_1, a_2, ..., a_n.
# Визначити суму та кількість додатних елементів,
# індекси яких діляться на 3 без остачі.

lst = [int(e) for e in input().split()]

#lst = [1, -20, 50, 10000, -2, 11, 15, 1, 20000, -20, -20]
#      0   1    2    3    4    5   6  7    8     9    10
#      ^             ^             ^             ^

# спосіб 1
sublist = lst[::3]
print(sublist)
print(sum(sublist), len(sublist))

# спосіб 2
s = 0
for i in range(len(lst)):
    print(i, '--->', lst[i])
    if i % 3 == 0:
        s = s + lst[i]
print('>>', s)



