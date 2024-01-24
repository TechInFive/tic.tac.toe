import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.options = [
            'Easy Mode - Player First', 
            'Easy Mode - AI First',
            'Hard Mode - Player First', 
            'Hard Mode - AI First', 
            'Free Play'
        ]
        self.font = pygame.font.Font(None, 28)
        self.option_rects = []

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.option_rects.clear()
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option, True, (255, 255, 255))
            x = 50  # Horizontal position
            y = 50 + i * 44  # Vertical position, spaced for each option
            self.screen.blit(text_surface, (x, y))
            self.option_rects.append(text_surface.get_rect(topleft=(x, y)))
        pygame.display.update()

    def get_selection(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(mouse_pos):
                        return self.handle_option_selection(i)
        return 'waiting', None

    def handle_option_selection(self, option_index):
        if option_index == 0:
            return 'easy', 'player'
        elif option_index == 1:
            return 'easy', 'ai'
        elif option_index == 2:
            return 'hard', 'player'
        elif option_index == 3:
            return 'hard', 'ai'
        elif option_index == 4:
            return 'freeplay', None
