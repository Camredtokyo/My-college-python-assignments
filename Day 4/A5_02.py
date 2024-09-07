#A5_02. write a program to multiply two matrices as nested lists.

matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

rows_A = len(matrix_A)
cols_A = len(matrix_A[0])
rows_B = len(matrix_B)
cols_B = len(matrix_B[0])

result = [[0] * cols_B for _ in range(rows_A)]

for i in range(rows_A):
    for j in range(cols_B):
        sum = 0
        for k in range(cols_A):
            sum += matrix_A[i][k] * matrix_B[k][j]
        result[i][j] = sum

for row in result:
    print(row)
