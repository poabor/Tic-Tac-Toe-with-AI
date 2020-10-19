import textwrap
import random


class Tictactoe:

    def __init__(self, user1, user2):
        self.devider = '-' * 9
        self.matrix = []
        self.correct_input = False
        self.game_state = 'Game not finished'
        self.symX = 'X'
        self.symO = 'O'
        self.user1 = user1
        self.user2 = user2
        self.rand = 0

    def first_init(self, cells):
        rows = textwrap.wrap(cells, 3)
        for row in rows:
            self.matrix.append([x for x in row])

    def action(self, user, symbol):
        self.do_move(user, symbol)
        self.print_matrix()

    def action_game(self):
        self.print_matrix()
        while True:
            self.action(self.user1, self.symX)
            if self.game_state != 'Game not finished':
                break
            self.action(self.user2, self.symO)
            if self.game_state != 'Game not finished':
                break
        print(self.game_state)

    @staticmethod
    def convert_user_move(user_list):
        rows = [2, 1, 0]
        user_list.reverse()
        u_list = list(map(int, user_list))
        return [rows[u_list[0] - 1], u_list[1] - 1]

    def get_user_coordinate(self, user_list):
        if len([x for x in user_list if x.isdigit()]) != 2:
            print('You should enter numbers!')
        elif len([x for x in user_list if int(x) > 3]) > 0 or len([x for x in user_list if int(x) < 1]) > 0:
            print('Coordinates should be from 1 to 3!')
        else:
            return self.convert_user_move(user_list)
        return None

    def get_easy_coordinate(self):
        self.rand += 1
        random.seed(self.rand)
        return [int(random.choice('012')), int(random.choice('012'))]

    def get_medium_coordinate(self, symbol, get_easy=False):
        for i in range(0, 3):  # row
            if self.matrix[i].count(symbol) == 2 and self.matrix[i].count('_') == 1:
                return [i, self.matrix[i].index('_')]
        for j in range(0, 3):  # column
            col = []
            for i in range(0, 3):
                col.append(self.matrix[i][j])
            if col.count(symbol) == 2 and col.count('_') == 1:
                return [col.index('_'), j]
        diag_right = []
        diag_left = []
        for i in range(0, 3):  # diagonal
            diag_right.append(self.matrix[i][i])
            diag_left.append(self.matrix[3 - i - 1][i])
        if diag_right.count(symbol) == 2 and diag_right.count('_') == 1:
            return [diag_right.index('_'), diag_right.index('_')]
        if diag_left.count(symbol) == 2 and diag_left.count('_') == 1:
            return [diag_left.index('_'), diag_left.index('_')]
        if get_easy:
            return self.get_easy_coordinate()
        else:
            return [0, 0]

    def empty_indexes(self, board):
        return [i for i, j in enumerate(board) if str(j) not in 'XO']


    def wining(self, board, player):
        if ((board[0] == player and board[1] == player and board[2] == player) |
                (board[3] == player and board[4] == player and board[5] == player) |
                (board[6] == player and board[7] == player and board[8] == player) |
                (board[0] == player and board[3] == player and board[6] == player) |
                (board[1] == player and board[4] == player and board[7] == player) |
                (board[2] == player and board[5] == player and board[8] == player) |
                (board[0] == player and board[4] == player and board[8] == player) |
                (board[2] == player and board[4] == player and board[6] == player)):
            return True
        else:
            return False

    def minimax(self, newBoard, player):
        if player == self.symO:
            hu_player = self.symX
        else:
            hu_player = self.symO
        avail_spots = self.empty_indexes(newBoard)
        if self.wining(newBoard, hu_player):
            return {'score': -10}
        elif self.wining(newBoard, player):
            return {'score': 10}
        elif len(avail_spots) == 0:
            return {'score': 0}
        moves = []
        for i in avail_spots:
            move = {}
            move['index'] = i  # newBoard[avail_spots[i]]
            newBoard[i] = player
            if player == player:
                result = self.minimax(newBoard, hu_player)
                move['score'] = result['score']
            else:
                result = self.minimax(newBoard, player)
                move['score'] = result['score']
            newBoard[i] = move['index']
            moves.append(move)
        if player == player:
            best_score = -10000
            for j, i in enumerate(moves):
                if i['score'] > best_score:
                    best_score = i['score']
                    best_move = j
        else:
            best_score = 10000
            for j, i in enumerate(moves):
                if i['score'] < best_score:
                    best_score = i['score']
                    best_move = j
        return moves[best_move]

    def get_hard_coordinate(self, symbol):
        flat_matrix = []
        for i in self.matrix:
            for j in i:
                flat_matrix.append(j)
        best_move = self.minimax(flat_matrix, symbol)
        print(best_move)
        if best_move['index'] <= 2:
            i = 0
        elif best_move['index'] <= 5:
            i = 1
        else:
            i = 2
        j = best_move['index'] % 3
        # print('j ' + str(j))
        return [i, j]

    def do_move(self, user, symbol):
        """
        @type user: str
        @type symbol: str
        """
        while not self.correct_input:
            is_user = (user == 'user')
            if is_user:
                user_list = input('Enter the coordinates: ').split()
                if user_list[0] == 'exit':
                    self.game_state = 'exit'
                    break
                else:
                    in_list = self.get_user_coordinate(user_list)
            elif user == 'medium':
                in_list = self.get_medium_coordinate(symbol)  # check user can win
                if in_list == [0, 0]:
                    other_sym = self.symX if symbol == self.symO else self.symO
                    in_list = self.get_medium_coordinate(other_sym, True)  # opponent can win
            elif user == 'hard':
                in_list = self.get_hard_coordinate(symbol)
            else:
                in_list = self.get_easy_coordinate()
            self.check_input(in_list, is_user)
            if self.correct_input:
                if not is_user:
                    print('Making move level "{}"'.format(user))
                self.matrix[in_list[0]][in_list[1]] = symbol
                self.set_state()
        self.correct_input = False

    def print_matrix(self):
        print(self.devider)
        for row in self.matrix:
            print('| ' + ' '.join(i.replace('_', ' ') for i in row) + ' |')
        print(self.devider)

    def check_input(self, in_list, is_user):
        if in_list == None:
            pass

        elif self.matrix[in_list[0]][in_list[1]] == '_':
            self.correct_input = True
        elif is_user:
            print('This cell is occupied! Choose another one!')

    def set_state(self):
        if self.check_diagonal(self.symX) or self.check_line(self.symX):
            self.game_state = self.symX + ' wins'
        elif self.check_diagonal(self.symO) or self.check_line(self.symO):
            self.game_state = self.symO + ' wins'
        elif not self.check_empty():
            self.game_state = 'Draw'

    def check_diagonal(self, symb):
        toright = True
        toleft = True
        for i in range(0, 3):
            toright &= (self.matrix[i][i] == symb)
            toleft &= (self.matrix[3 - i - 1][i] == symb)
        return toleft or toright

    def check_line(self, symb):
        for row in range(0, 3):
            cols = True
            rows = True
            for col in range(0, 3):
                cols &= (self.matrix[col][row] == symb)
                rows &= (self.matrix[row][col] == symb)
            if cols or rows:
                return True
        return cols or rows

    def check_empty(self):
        for col in range(0, 3):
            for row in range(0, 3):
                if self.matrix[col][row] == '_':
                    return True
        return False


while True:
    in_string = input('Input command: ').split()
    if in_string[0] == 'exit':
        break
    if in_string[0] == 'start':
        if len(in_string) != 3:
            print('Bad parameters!')
        else:
            main_game = Tictactoe(in_string[1], in_string[2])
            start_board = 'O_XX_X_OO'
            start_board = '_________'
            main_game.first_init(start_board)
            main_game.action_game()
            if main_game.game_state == 'exit':
                break
