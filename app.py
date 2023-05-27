import pygame as pg
import sys

from main_menu import MainMenu
from tetris import NewGame

class App:
    def __init__(self) -> None:
        self.run()
    
    def run(self):
        menu_return = MainMenu().main()
        
        if menu_return == 'new_game':
            self.start_game()
        elif menu_return == 'options':
            self.options()
        elif menu_return == 'exit':
            self.quit()
    
    def start_game(self):
        tetris = NewGame().main()

    def options(self):
        # todo... for now, rerun MainMenu
        self.run()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    app = App()
