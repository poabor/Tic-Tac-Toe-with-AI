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
            print('row: ' + str(i + 1))
            return [matrix[i].index('_') + 1, i + 1]
    for j in range(0, 3):  # column
        col = []
        for i in range(0, 3):
            col.append(matrix[i][j])
        if col.count(symbol) == 2 and col.count('_') == 1:
            print('col: ' + str(j + 1))
            return [j + 1, self_rows[col.index('_')] + 1]
    toright = []
    toleft = []
    for i in range(0, 3):  # diagonal
        toright.append(matrix[i][i])
        toleft.append(matrix[3 - i - 1][i])
    if toright.count(symbol) == 2 and toright.count('_') == 1:
        print('toright: ' + str(toright))
        #return [str(self_rows[toright.index('_')] + 1), str(toright.index('_') + 1)]
        return [str(toright.index('_') + 1), str(toright.index('_') + 1)]
    if toleft.count(symbol) == 2 and toleft.count('_') == 1:
        print('toleft: ' + str(toleft), toleft.index('_'))
        return [str(toleft.index('_') + 1), str(toleft.index('_') + 1)]

    print(toright)
    print(toleft)
    return ['0', '0']

def check_line(matrix, symb):
    for row in range(0, 3):
        cols = True
        rows = True
        for col in range(0, 3):
            rows &= (matrix[row][col] == symb)
            cols &= (matrix[col][row] == symb)
        if cols or rows:
            return True
    return cols or rows

def check_input(matrix, var_input):
    self_rows = [2, 1, 0]
    #i = self_rows[int(var_input[1]) - 1]
    i = int(var_input[1]) - 1
    j = int(var_input[0]) - 1
    if matrix[i][j] == '_':
        print('correct_input')
    else:
        print('This cell is occupied! Choose another one!')

def in_user():
    self_rows = [2, 1, 0]
    in_list_user = input('Enter the coordinates: ').split()
    if in_list_user[0] == 'exit':
        in_list = 'exit'
    else:
        in_list_user.reverse()
        in_list1 = list(map(int, in_list_user))
        in_list = [self_rows[in_list1[0] - 1], in_list1[1] - 1]
    return in_list

matrix = first_init('X_OOXXX__')
print_matrix(matrix)
in_list = get_medium_coordinate(matrix, 'X')
# print(in_list)
# check_input(matrix, in_list)
#print('line: ', check_line(matrix, 'O'))
#print(in_user())