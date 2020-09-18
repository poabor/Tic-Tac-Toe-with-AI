import textwrap
import random


#
# class Player:
#
#     def __init__(self, level):
#         self.level = level
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()

def first_init(cells):
    matrix = []
    rows = textwrap.wrap(cells, 3)
    for row in rows:
        matrix.append([x for x in row])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print('| ' + ' '.join(i.replace('_', ' ') for i in row) + ' |')


def get_medium_coordinate(matrix, symbol):
    self_rows = [2, 1, 0]
    for i in range(0, 3):  # row
        if matrix[i].count(symbol) == 2 and matrix[i].count('_') == 1:
            return [self_rows[matrix[i].index('_')] + 1, self_rows[i] + 1]
    for j in range(0, 3):  # column
        col = []
        for i in range(0, 3):
            col.append(matrix[i][j])
        if col.count(symbol) == 2 and col.count('_') == 1:
            return [col.index('_') + 1, j + 1]
    toright = []
    toleft = []
    for i in range(0, 3):  # diagonal
        toright.append(matrix[i][i])
        toleft.append(matrix[3 - i - 1][i])
    if toright.count(symbol) == 2 and toright.count('_') == 1:
        return [toright.index('_') + 1, i]
    if toleft.count(symbol) == 2 and toleft.count('_') == 1:
        return [toleft.index('_') + 1, i]

    print(toright)
    print(toleft)
    return [0, 0]


matrix = first_init('_XXXOO_XO')
print_matrix(matrix)
print(get_medium_coordinate(matrix, 'X'))
