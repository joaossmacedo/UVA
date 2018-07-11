# -1 return means that every row/column is even
# -2 return means that 2 or more rows/columns are odd
# a positive number return means that this number row/column is odd


def check_rows(matrix: list, n: int) -> int:
    unbalanced_row = -1
    already_unbalanced = False

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += int(matrix[i][j])
        if sum % 2 != 0:
            if already_unbalanced:
                unbalanced_row = -2
                return unbalanced_row

            unbalanced_row = i
            already_unbalanced = True

    return unbalanced_row


def check_columns(matrix: list, n: int) -> int:
    unbalanced_column = -1
    already_unbalanced = False

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += int(matrix[j][i])
        if sum % 2 != 0:
            if already_unbalanced:
                unbalanced_column = -2
                return unbalanced_column

            unbalanced_column = i
            already_unbalanced = True

    return unbalanced_column


while True:
    matrix = []

    n = int(input())

    if n == 0:
        exit()

    for i in range(n):
        matrix.append(input().replace('\n', '').split())

    unbalanced_column = check_columns(matrix, n)
    unbalanced_row = check_rows(matrix, n)

    if unbalanced_column == -1 and unbalanced_row == -1:
        print('OK')
    elif unbalanced_column == -1 or unbalanced_row == -1:
        print('Corrupt')
    elif unbalanced_column == -2 or unbalanced_row == -2:
        print('Corrupt')
    else:
        print('Change bit ', end = '')
        print('(' + str(unbalanced_row + 1) + ',' + str(unbalanced_column + 1) + ')')
