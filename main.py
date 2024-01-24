# main.py
import pygame
import sys

from game_state_manager import GameStateManager

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

# Initialize GameStateManager
game_state_manager = GameStateManager(screen)

# Main game loop
while game_state_manager.running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pass events into game state manager
    game_state_manager.update(events)

    # Update the display
    pygame.display.update()
