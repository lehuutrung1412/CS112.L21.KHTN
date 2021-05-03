def inRow(row, value):
    if value in matrix[row]:
        return True
    return False


def inCol(col, value):
    for i in range(9):
        if value == matrix[i][col]:
            return True
    return False


def inBox(row, col, value):
    for i in range(row*3, row*3+3):
        for j in range(col*3, col*3+3):
            if matrix[i][j] == value:
                return True
    return False


def isValid(row, col, value):
    return not inRow(row, value) and not inCol(col, value) and not inBox(row//3, col//3, value)


def isSolved(matrix):
    for i in range(9):
        if 0 in matrix[i]:
            return False
    return True


def printSudoku(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end=' ')
        print()


def solve(row, col):
    if isSolved(matrix):
        return True
    if col == 9:
        return solve(row + 1, 0)
    if matrix[row][col] == 0:
        for num in range(1, 10):
            if isValid(row, col, num):
                matrix[row][col] = num
                if solve(row, col + 1):
                    return True
            matrix[row][col] = 0
    else:
        return solve(row, col + 1)
    return False


if __name__ == '__main__':
    matrix = []
    for i in range(9):
        lRow = list(map(int, input().split()))
        matrix.append(lRow)
    print()
    if solve(0, 0):
        printSudoku(matrix)
    else:
        print(-1)