import pygame

class GameOver:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def draw(self):
        # Draw the game over message
        text_game_over = pygame.font.Font(None, 36).render("Game Over!", True, (255, 255, 255))
        self.screen.blit(text_game_over, (50, 50))

        text_options = pygame.font.Font(None, 24).render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        self.screen.blit(text_options, (50, 100))
        pygame.display.update()

    def get_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                elif event.key == pygame.K_q:
                    return 'quit'
        return None
