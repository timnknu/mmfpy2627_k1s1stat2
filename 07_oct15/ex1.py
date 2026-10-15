a = [1,2,3,3]

# print(100500 in a)
# print(a.index(100500))
# if el in a:
#   idx = a.index(el)
# else:
#   idx = -1

b = ['e', '*']

L = a + b
print(L)

#L = a + b + b + b + b + b
L = a + b * 5
#L = a + 5 * b
print(L)

b = [0]
L = [] + b * 5
print(L)

L = [0] * 10
print(L)