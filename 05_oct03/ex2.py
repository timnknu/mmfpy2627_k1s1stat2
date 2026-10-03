xfirst = 10
x2 = -2
x3 = 90
x4 = 5
x5 = 8

avg = (xfirst + x2 + x3 + x4 + x5)/5
print(avg)

my_list = [10, -2, 90, 5, x5]
print(my_list)
print(f'список {my_list} містить він {len(my_list)} елементів')

b = (my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4])/5
print(b)

n_elems = len(my_list)
s = 0
for i in range(n_elems):
    print('element #', i, ' is ->', my_list[i])
    s = s + my_list[i]
print(s / n_elems)


print(sum(my_list) / n_elems)