import operator


def determinant(matrix):
    length = len(matrix)
    matrix_determinant = 1
    count = 0
    if matrix[0][0] == 0:
        matrix[0], matrix[1] = matrix[1], matrix[0]
        matrix_determinant *= -1
    if length > 2:
        for yx in range(length - 1):
            if matrix[yx][yx + 1] == matrix[yx + 1][yx + 1]:
                count += 1
                if count == length:
                    return 0
                try:
                    matrix[yx + 1], matrix[yx + 2] = matrix[yx + 2], matrix[yx + 1]
                    matrix_determinant *= -1
                    yx = 0
                except:
                    matrix[yx], matrix[yx - 1] = matrix[yx - 1], matrix[yx]
                    matrix_determinant *= -1
    if length == 1:
        return matrix[0][0]
    elif length == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    else:
        for i in range(length):
            try:
                j = i
                k = i + 1
                l = 1
                while k < length:
                    if matrix[i][j] != 0:
                        a = (matrix[i + l][j] / matrix[i][j]) * -1
                        list_copy = [a * x for x in matrix[i]]
                    else:
                        list_copy = None
                    matrix[k] = list(map(operator.add, matrix[k], list_copy))
                    k += 1
                    l += 1
            except:
                continue
        for i in range(length):
            matrix_determinant *= matrix[i][i]
        return round(matrix_determinant)


# print(determinant([[1,3], [2,5]]))
print(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]))
print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))
print(determinant([[2, 5, 3, -1], [1, -2, -1, 0], [1, 3, 4, -3], [2, 1, -1, 3]]))
print(
    determinant(
        [
            [2, 4, 5, 3, 1, 2],
            [2, 4, 7, 5, 3, 2],
            [1, 1, 0, 2, 3, 1],
            [1, 3, 9, 0, 3, 2],
            [1, 1, 2, 2, 4, 1],
            [0, 0, 4, 1, 2, 3],
        ]
    )
)
