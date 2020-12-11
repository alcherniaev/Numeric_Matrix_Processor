# sum one matrix with another
def sum_matrix():
    # getting an input
    n, m = list(map(int, input().split()))  # matrix size n*m
    matrix_1 = []

    # constructing matrix from input
    for i in range(n):
        matrix_1.append(list(map(int, input().split())))

    # repeat with second matrix
    n_1, m_1 = list(map(int, input().split()))
    matrix_2 = []

    # checking if it's possible to sum (matrix must be same size)
    if n == n_1 and m == m_1:
        for i in range(n_1):
            matrix_2.append(list(map(int, input().split())))

        # initialize zero-matrix for future changing with needed number
        matrix_sum = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]
        for i in matrix_sum:
            print(*i)
    else:
        print('ERROR')


# multiply matrix with any constant
def multiply_by_const():
    # getting size, matrix and constant from input
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for j in range(n)]
    x = int(input())
    # multiply matrix by a constant
    matrix_by_x = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            matrix_by_x[i][j] = x * matrix[i][j]
    for i in matrix_by_x:
        print(*i)



