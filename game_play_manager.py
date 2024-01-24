import pygame
from tic_tac_toe import BOARD_COLS, BOARD_ROWS

# Constants for the game
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

class GamePlayManager:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def draw_board(self):
        self.screen.fill(BG_COLOR)
        # Draw the Tic-Tac-Toe grid lines
        self.draw_lines()

        # Draw the X's and O's based on the game state
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.game.board[row][col] == 1:
                    self.draw_x(row, col)
                elif self.game.board[row][col] == 2:
                    self.draw_o(row, col)

    def draw_lines(self):
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_o(self, row, col):
        pygame.draw.circle(self.screen, GREEN, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), 
                            int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

    def draw_x(self, row, col):
        pygame.draw.line(self.screen, RED, 
                        (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                        (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                        CROSS_WIDTH)
        pygame.draw.line(self.screen, RED, 
                        (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                        (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                        CROSS_WIDTH)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game.game_over:
                self.handle_mouse_click(event.pos)

    def handle_mouse_click(self, pos):
        row, col = self.get_row_col_from_mouse(pos)
        if self.game.available_square(row, col):
            self.game.mark_square(row, col)
            self.update_board(row, col)

            if self.game.check_win():
                self.game.game_over = True
            elif self.game.check_draw():
                self.game.game_over = True
            else:
                self.game.toggle_player()
                self.handle_ai_move()

    def update_board(self, row, col):
        if self.game.board[row][col] == 1:
            self.draw_x(row, col)
        elif self.game.board[row][col] == 2:
            self.draw_o(row, col)

    def handle_ai_move(self):
        # AI move logic for 'easy' or 'hard' mode
        pass

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
