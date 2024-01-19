BOARD_ROWS = 3
BOARD_COLS = 3

class TicTacToe:
    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 1
        self.game_over = False

    def available_square(self, row, col):
        return self.board[row][col] is None

    def mark_square(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
        return False

    def check_win(self):
        # Check rows, columns and diagonals for a win
        mark = self.current_player
        for row in range(BOARD_ROWS):
            if self.board[row][0] == mark and self.board[row][1] == mark and self.board[row][2] == mark:
                return True
        for col in range(BOARD_COLS):
            if self.board[0][col] == mark and self.board[1][col] == mark and self.board[2][col] == mark:
                return True
        if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark:
            return True
        if self.board[0][2] == mark and self.board[1][1] == mark and self.board[2][0] == mark:
            return True
        return False 

    def check_draw(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] is None:
                    return False
        return True

    def toggle_player(self):
        self.current_player = self.current_player % 2 + 1

    def reset_game(self):
        self.__init__()
