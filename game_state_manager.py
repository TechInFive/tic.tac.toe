from game_over import GameOver
from game_play_manager import GamePlayManager
from menu import Menu
from tic_tac_toe import TicTacToe

class GameStateManager:
    def __init__(self, screen):
        self.state = 'menu'
        self.screen = screen
        self.menu = Menu(screen)
        self.game = None
        self.game_over = None
        self.running = True

    def update(self, events):
        if self.state == 'menu':
            self.handle_menu(events)
        elif self.state == 'game':
            self.handle_game(events)
        elif self.state == 'game_over':
            self.handle_game_over(events)

    def handle_menu(self, events):
        mode, turn = self.menu.get_selection(events)
        if mode == 'waiting':
            self.menu.draw()
        else:
            self.game = TicTacToe(mode, turn)
            self.state = 'game'
            self.game_play_manager = GamePlayManager(self.screen, self.game)

    def handle_game(self, events):
        self.game_play_manager.draw_board()
        self.game_play_manager.handle_events(events)
        if self.game.game_over:
            self.state = 'game_over'

    def handle_game_over(self, events):
        if not self.game_over:
            self.game_over = GameOver(self.screen, self.game)

        self.game_over.draw()
        action = self.game_over.get_input(events)

        if action == 'restart':
            self.state = 'menu'
            self.menu = Menu(self.screen)
            self.game_over = None
        elif action == 'quit':
            self.running = False
