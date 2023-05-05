import pygame as pg
import sys

from main_menu import MainMenu
from tetris import NewGame

class App:
    def __init__(self) -> None:
        self.run()
    
    def run(self):
        print('starting run..')
        menu_return = MainMenu().main_loop()
        # from mainMenu:
        #   if main_return is 'new game' -> call start_game() to run new game
        #   elif main_return is 'exit' -> quit game
        #   elif main_return is 'options' -> call options() to run options
        #   else -> rerun mainMenu
        if menu_return == 'new game':
            self.start_game()
        elif menu_return == 'options':
            self.options()
        elif menu_return == 'exit':
            self.quit()
    
    def start_game(self):
        tetris = NewGame()

    def options(self):
        # todo... for now, rerun MainMenu
        self.run()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    app = App()
