def ask_length(side_name):
    while True:
        a1 = input(f"введіть сторону {side_name}")
        try:
            a = float(a1)
            if a < 0:
                raise ValueError(111, 222, 333)
            break
        except ValueError as e:
            print(e.args)
            if len(e.args) > 1:
                print('від\'ємну сторону ввести не можна')
            else:
                print('введено некоректне число!')
    return a
#

a = ask_length('a')
b = ask_length('b')
c = ask_length('c')

assert c < a+b
assert a < c+b
assert b < a+c

p = (a+b+c)/2
print('p=', p)
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)
