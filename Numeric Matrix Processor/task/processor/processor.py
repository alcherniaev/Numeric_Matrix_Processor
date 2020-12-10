n, m = list(map(int, input().split()))
matrix_1 = []
for i in range(n):
    matrix_1.append(list(map(int, input().split())))

n_1, m_1 = list(map(int, input().split()))
matrix_2 = []
for i in range(n_1):
    matrix_2.append(list(map(int, input().split())))
#matrix_sum = [x + y for x, y in zip(matrix_1, matrix_2)]
#matrix_sum = [[0 for i in range(n)] for j in range(m)]

matrix = [input().split() for i in range(row)]
matrix_sum_0 = []
matrix_sum_1 = []
matrix_sum = matrix_sum_0 + matrix_sum_1
for x, y in zip(matrix_1[:n/2], matrix_2[:n/2]):
    for x_, y_ in zip(x, y):
        matrix_sum_0.append(x_+y_)

for x, y in zip(matrix_1[n/2:], matrix_2[n/2:]):
    for x_, y_ in zip(x, y):
        matrix_sum_1.append(x_+y_)

print(matrix_sum)
