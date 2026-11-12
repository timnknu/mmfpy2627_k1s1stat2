L = [1, 'h', [1,3], 'h', 1, 1]

#print(set(L))

A = list(range(1, 1000, 2))
print(A)
print('>>', 15 in A)

# 3 -> 9
# 4 -> 16
# ...
d = {}
for x in A:
    d[x] = x**2
print(d)

print('##', 15 in d)

s = set(A)
print(s)
print('++', 15 in s)

B = {
    1: 'hello',
    ('cat', 'dot'): 'world'
}
print(B)