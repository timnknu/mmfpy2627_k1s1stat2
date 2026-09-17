# 2.3. Хоча б одна умова з двох
# Для заданого цілого числа n вивести відповідь YES, якщо виконується
# хоча б одна з наступних умов і NO у протилежному випадку.
# • число n непарне;
# • число n додатне і трицифрове.

n = int(input())
#n = 900

# print(n == 15)
# print(n == 32)
# print(n != 32)

cond1 = n % 2 == 1 # число n непарне
is_positive = n > 0
has_3_digits = (n <= 999) and (n >= 100) #   число<=999 і водночас число>=100

print(cond1, is_positive, has_3_digits)

pos_3_dig = is_positive and has_3_digits # чи "число n додатне і трицифрове"
#pos_3_dig = (n > 0) and ((n <= 999) and (n >= 100))


if cond1 or pos_3_dig:
    print("YES")
else:
    print("NO")

