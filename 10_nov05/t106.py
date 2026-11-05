def print_matrix(A, n='Матриця:'):
    print(n)
    for r in A:
        for item in r:
            print(f'{item:8}', end='  ')
        print()

####

A = [    [1, 0], [0, 1]  ]
B = [   [2, 3],  [15, -1.2]  ]

print_matrix(A, 'перший співмножник')
print_matrix(B, 'другий співмножник')


def multiply_matrices(P, Q, matrix_size):

    def get_result_elem(i, j):
        elem = 0
        for r in range(matrix_size):
            elem = elem + P[i][r] * Q[r][j]
        # print('C[0][0] == ', elem)
        return elem

    C = []
    for k in range(matrix_size):
        row = []
        for d in range(matrix_size):
            row.append( get_result_elem(k, d) )
        C.append(row)
    #
    return C

resM = multiply_matrices(A, B, 2)
print_matrix(resM)

E = [    [1, 0, 0], [0, 1, 0], [0, 0, 1]  ]
F = [   [82, 83, -79],  [815, -81.2, 81], [-82, 815, 85]  ]

C = multiply_matrices(E, F, 3)
print_matrix(C)