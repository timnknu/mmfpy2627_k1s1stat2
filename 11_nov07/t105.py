def print_matrix(A, n='Матриця:'):
    print(n)
    for r in A:
        for item in r:
            print(f'{item:8}', end='  ')
        print()

####

A = [
    [1, 2, 3],
    [2, 3, 4],
    [2, 1, 1]
     ]
# len(A) == len(A[0]) == len(A[1]) == len(A[2]) == ...

print_matrix(A)

# B = [
#     [ 2, 3],
#     [ 1, 1]
#      ]

# A = []
# for i in range(3):
#     row = [int(d) for d in input().split()]
#     A.append(row)


def det(M):
    if len(M) == 1:
        # якщо нам передали матрицю розміром 1х1
        row = M[0]
        return row[0]
    else:
        # якщо нам передали матрицю більшого розміру
        res = 0
        n = len(M)
        for r in range(n):
            B = []
            for k, row in enumerate(M):
                if k != r:
                    B.append(row[1:])
            d = det(B)
            res = res + (-1)**(0+r) * M[r][0] * d

        return res



r = det(A)
print(r)
