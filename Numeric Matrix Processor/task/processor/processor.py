n, m = list(map(int, input().split()))
matrix_1 = []
for i in range(n):
    matrix_1.append(list(map(int, input().split())))

n_1, m_1 = list(map(int, input().split()))
matrix_2 = []
for i in range(n_1):
    matrix_2.append(list(map(int, input().split())))
#matrix_sum = [x + y for x, y in zip(matrix_1, matrix_2)]

matrix_sum = [[0 for i in range(m)] for j in range(n)]
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]

print(matrix_sum)
