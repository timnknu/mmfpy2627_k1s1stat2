import math
import copy

a = [1, -2]   # a[0] == ax, a[1] == ay
b = [3, 4.8]  # b[0] == bx, b[1] == by

def vector_length(v):
    L = copy.deepcopy(v)
    res = math.sqrt(L[0]**2 + L[1]**2)
    L[0] = -100000
    print('L=', L)
    return res


###


la = vector_length(a)
lb = vector_length(b)

print(la, lb)

print(a)