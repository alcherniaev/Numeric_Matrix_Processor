# sum one matrix with another
def sum_matrix():
    # getting an input
    n, m = list(map(int, input('Enter size of first matrix: > ').split()))  # matrix size n*m
    matrix_1 = []

    # constructing matrix from input
    print('Enter first matrix: ')
    for i in range(n):
        matrix_1.append(list(map(float, input('> ').split())))

    # repeat with second matrix
    n_1, m_1 = list(map(int, input('Enter size of second matrix: > ').split()))
    matrix_2 = []

    # checking if it's possible to sum (matrix must be same size)
    if n == n_1 and m == m_1:
        print('Enter second matrix: ')
        for i in range(n_1):
            matrix_2.append(list(map(float, input('> ').split())))

        # initialize zero-matrix for future changing with needed number
        matrix_sum = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]
        print('The result is: ')
        for i in matrix_sum:
            print(*i)
        return None
    else:
        print('ERROR')
        return None


# multiply matrix by any constant
def multiply_by_const():
    # getting size, matrix and constant from input
    n, m = map(int, input('Enter size of matrix: > ').split())
    matrix = [list(map(float, input('Enter matrix: ').split())) for j in range(n)]
    x = int(input('Enter constant: > '))
    # multiply matrix by a constant
    matrix_by_x = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            matrix_by_x[i][j] = x * matrix[i][j]
    print('The result is: ')
    for i in matrix_by_x:
        print(*i)
    return None


# multiply matrix by matrix
def multiply_by_matrix():
    # getting an input
    n, m = list(map(int, input('Enter size of first matrix: > ').split()))  # matrix size n*m
    matrix_1 = []

    # constructing first matrix from input
    print('Enter first matrix: ')
    for i in range(n):
        matrix_1.append(list(map(float, input('> ').split())))

    # repeat with second matrix
    n_1, m_1 = list(map(int, input('Enter size of second matrix: > ').split()))
    matrix_2 = []

    # constructing second matrix from input
    print('Enter second matrix: ')
    for i in range(n_1):
        matrix_2.append(list(map(float input('> ').split())))
    if len(matrix_1[0]) != len(matrix_2):
        return None
    new_matrix = [[sum([a * b for a, b in zip(A_row, B_col)]) for B_col in zip(*matrix_2)] for A_row in matrix_1]
    print('The result is: ')
    for i in new_matrix:
        print(*i)
    return None


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    return int(input("Your choice: > "))


choice = menu()

#while choice != 0:
if choice == 1:
    sum_matrix()
elif choice == 2:
    multiply_by_const()
elif choice == 3:
    multiply_by_matrix()
elif choice == 0:
    pass
