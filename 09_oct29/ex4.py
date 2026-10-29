def print_matrix(A):
    print('Here is a matrix:')
    for r in A:
        for item in r:
            print(f'{item:8}', end='    ')
        print()

####

row1 = [1, 15, -8.2, 4.9]
row2 = [-8, 4, 5, 12.1]
row3 = [0, 0, 82, 1.5]

M = [row1, row2, row3]

print(M)

print_matrix(M)

L = [[2, 3], [15, -1.2]]
print_matrix(L)


