
import sys
import pygame as pg
from pygame.locals import *
import config
from models.text_item import TextItem
import utils.color_dict as color_dict

color_dict = color_dict.ColorDict().colors

class MainMenu():
    def __init__(self):
        self.surface = pg.display.set_mode((config.window['width'], config.window['height']))
        self.menu_items = {}
        
        pg.init()
        pg.display.set_caption(config.title)

        self.clock = pg.time.Clock()
        
        self.main_loop()

    def main_loop(self):
        self.background = pg.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(color_dict['black'])

        self.menu_items = {
            "new_game": TextItem(0.3175, 0.5, 0.365, "New Game", self.surface, True, 8),
            "options": TextItem(0.37, 0.625, 0.26, "Options", self.surface, True, 8),
            "exit": TextItem(0.4313, 0.75, 0.1375, "Exit", self.surface, True, 8)
        }
        self.title_text = TextItem(0.3, 0.1, 0.7, config.title, self.surface, False, 14)

        self.surface.blit(self.background, (0, 0))
        pg.display.flip()

        self.draw_game_screen()
        
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                elif event.type == pg.MOUSEMOTION:
                    mouse = pg.mouse.get_pos()
                    if self.menu_items['new_game'].isHover(mouse):
                        highlighted = 1
                    elif self.menu_items['options'].isHover(mouse):
                        highlighted = 2
                    elif self.menu_items['exit'].isHover(mouse):
                        highlighted = 3
                    else:
                        highlighted = 0
                    self.draw_game_screen(highlighted)
            
                elif event.type == pg.MOUSEBUTTONDOWN:
                    highlighted = 0
                    mouse = pg.mouse.get_pos()
                    click = pg.mouse.get_pressed()
                    if click[0] == 1:
                        if self.menu_items['new_game'].isHover(mouse):
                            return 'new game'
                        elif self.menu_items['options'].isHover(mouse):
                            return 'options'
                        elif self.menu_items['exit'].isHover(mouse):
                            return 'exit'

            pg.display.flip()
            self.clock.tick(60)
        
        self.quit()

    def draw_game_screen(self, highlighted=0):
        # draw outline
        self.draw_outline()

        # draw game title to screen
        self.draw_title()

        # draw options to screen
        self.draw_menu_options(highlighted)
  
    def draw_outline(self):
        outline = Rect(
            config.border_buffer - config.border_thickness,
            config.border_buffer - config.border_thickness,
            config.board_width + (2 * config.border_thickness),
            config.board_width + (2 * config.border_thickness)
        )
        pg.draw.rect(
            surface=self.surface,
            color=color_dict['off_white'],
            rect=outline,
            width=config.border_thickness
        )
  
    def draw_title(self):
        self.title_text.draw(False)
    
    def draw_menu_options(self, highlighted=0):
        self.menu_items['new_game'].draw((highlighted == 1))
        self.menu_items['options'].draw((highlighted == 2))
        self.menu_items['exit'].draw((highlighted == 3))

    def quit(self):
        pg.quit()