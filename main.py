import pygame
import sys

from tic_tac_toe import BOARD_COLS, TicTacToe

# Initialize Pygame
pygame.init()

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

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Function to draw lines for the game board
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw an 'O'
def draw_o(row, col):
    pygame.draw.circle(screen, GREEN, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), 
                                     int(row * SQUARE_SIZE + SQUARE_SIZE//2)), 
                       CIRCLE_RADIUS, CIRCLE_WIDTH)

# Function to draw an 'X'
def draw_x(row, col):
    pygame.draw.line(screen, RED, 
                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                     CROSS_WIDTH)
    pygame.draw.line(screen, RED, 
                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                     CROSS_WIDTH)

# Function to display text on the screen
def display_text(text):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

game = TicTacToe()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            mouseX = event.pos[0]  # x coordinate of the click
            mouseY = event.pos[1]  # y coordinate of the click

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if game.available_square(clicked_row, clicked_col):
                game.mark_square(clicked_row, clicked_col)
                if game.current_player == 1:
                    draw_x(clicked_row, clicked_col)
                else:
                    draw_o(clicked_row, clicked_col)

                if game.check_win():
                    game.game_over = True
                    print(f"Player {game.current_player} wins!")
                elif game.check_draw():
                    game.game_over = True
                    print("It's a draw!")
                else:
                    game.toggle_player()

    # Inside the main loop
    if game.game_over:
        if game.check_draw():
            display_text("Draw!")
        else:
            display_text(f"Player {game.current_player} wins!")

        # Restart option after a delay
        pygame.time.wait(10000)  # Wait for 10 seconds before resetting
        game.reset_game()
        screen.fill(BG_COLOR)

    draw_lines()

    # Update the display
    pygame.display.update()
