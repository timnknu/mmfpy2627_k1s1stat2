L = [1]*5 + [2] + [1,2]
print(L)

# () -- tuple()
# [] -- list()
# {} -- dict() , set()


print(set(L))
# map(f, [1,3,4])
a = [int(x) for x in input('Inp1').split()]
b = map(int, input('Inp2').split())
# for x in b:
#     print('iteration:', x)
print('>>', a)
print('>>>', b,  list(b))