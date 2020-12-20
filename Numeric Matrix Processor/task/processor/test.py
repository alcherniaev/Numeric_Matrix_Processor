#B_col in zip(*matrix_2)

a = [[1, 7, 7], [6, 6, 4], [4, 2, 1]]

b = [x for x in zip(*a)]
print(a)
print([x for x in zip(*a)])
