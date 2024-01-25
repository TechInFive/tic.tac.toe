import random


BOARD_ROWS = 3
BOARD_COLS = 3

class TicTacToe:
    def __init__(self, mode):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 1
        self.game_over = False
        self.mode = mode

    def toggle_player(self):
        self.current_player = self.current_player % 2 + 1

    def available_square(self, row, col):
        return self.board[row][col] is None

    def mark_square(self, row, col):
        self.board[row][col] = self.current_player

    def check_win(self):
        return self.check_player_win(self.current_player)

    def check_player_win(self, player):
        # Check rows for a win
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check cols for a win
        for col in zip(*self.board):
            if all(cell == player for cell in col):
                return True
        # Check diagonal from top-left to bottom-right for a win
        if all(self.board[i][i] == player for i in range(BOARD_ROWS)):
            return True
        # Check diagonal from top-right to bottom-left for a win
        if all(self.board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_COLS)):
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

    def random_candidate(self, candidates):
        return random.choice(candidates) if candidates else None

    def find_player_win(self, player):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    # Place the player symbol temporarily
                    self.board[row][col] = player
                    # Check if this move wins the game
                    if self.check_player_win(player):
                        self.board[row][col] = None  # Reset the cell
                        return (row, col)
                    # Reset the cell after checking
                    self.board[row][col] = None
        return None

    def find_immediate_win(self):
        return self.find_player_win(self.current_player)

    def block_opponent_win(self):
        opponent = self.current_player % 2 + 1
        return self.find_player_win(opponent)

    def minimax(self, depth, is_maximizing, player):
        opponent = player % 2 + 1

        if self.check_player_win(player):
            return 1
        elif self.check_player_win(opponent):
            return -1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] is None:
                        self.board[row][col] = player
                        score = self.minimax(depth + 1, False, player)
                        self.board[row][col] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] is None:
                        self.board[row][col] = opponent
                        score = self.minimax(depth + 1, True, player)
                        self.board[row][col] = None
                        best_score = min(score, best_score)
            return best_score

    def get_available_moves(self):
        available_moves = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.available_square(row, col):
                    available_moves.append((row, col))

        return available_moves

    def find_best_move(self):
        available_moves = self.get_available_moves()
        if len(available_moves) == 9:
            return (1, 1)

        player = self.current_player

        best_score = -float('inf')
        best_move = None
        for available_move in available_moves:
            row = available_move[0]
            col = available_move[1]
            self.board[row][col] = player
            score = self.minimax(0, False, player)
            self.board[row][col] = None
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

    def random_pick(self):
        available_moves = self.get_available_moves()
        return self.random_candidate(available_moves)
