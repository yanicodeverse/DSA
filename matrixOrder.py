def matrixOrderCalc(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])

    return 'order of the matrix is {}x{}'.format(row_count, col_count)


if __name__ == "__main__":
    matrix = [[2, 3, 6], [-5, 9, -3]]
    print(matrixOrderCalc(matrix))
