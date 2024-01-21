BOARD_ROWS = 3
BOARD_COLS = 3

class TicTacToe:
    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 1
        self.game_over = False

    def toggle_player(self):
        self.current_player = self.current_player % 2 + 1

    def available_square(self, row, col):
        return self.board[row][col] is None

    def mark_square(self, row, col):
        self.board[row][col] = self.current_player

    def check_win(self):
        mark = self.current_player
        # Check rows for a win
        for row in self.board:
            if all(cell == mark for cell in row):
                return True
        # Check cols for a win
        for col in zip(*self.board):
            if all(cell == mark for cell in col):
                return True
        # Check diagonal from top-left to bottom-right for a win
        if all(self.board[i][i] == mark for i in range(BOARD_ROWS)):
            return True
        # Check diagonal from top-right to bottom-left for a win
        if all(self.board[i][BOARD_ROWS - 1 - i] == mark for i in range(BOARD_COLS)):
            return True
        return False 

    def check_draw(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] is None:
                    return False
        return True

    def reset_game(self):
        self.__init__()
