# Середнє з чисел
# Дано три різні числа a, b, c. Вивести середнє з них.
# Вхідні дані
# Числа a, b, c цілі та за модулем не перевищують 1000.

# a <= b <= c  ==> надрукувати b
# a <= c <= b  ==> надрукувати c

# b <= a <= c  ==> надрукувати a
# b <= c <= a  ==> надрукувати c

# c <= a <= b  ==> надрукувати a
# c <= b <= a  ==> надрукувати b


# a = int(input())
# b = int(input())
# c = int(input())

a, b, c = [int(d) for d in input("введіть три числа").split()]

if a <= b and a <= c: # чи a -- найменше з трьох ?
    if b <= c:
        print(b)  # адже a<=b<=c
    else:
        print(c)
elif b <= a and b <= c:  # чи b -- найменше з трьох ?
    if a <= c:
        print(a)
    else:
        print(c)
else: # отже -- займенше з трьох - це c
    if a <= b:
        print(a)
    else:
        print(b)
