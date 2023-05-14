
import sys
import pygame as pg
from pygame.locals import *
import config
from models.text_item import TextItem
import utils.color_dict as color_dict

color_dict = color_dict.ColorDict().colors

class MainMenu():
    def __init__(self):
        pg.init()
        pg.display.set_caption(config.title)

        self.surface = pg.display.set_mode((config.window['width'], config.window['height']))
        self.frame = pg.display.set_mode((config.window['width'], config.window['height']))
        self.menu_items = {}
        self.clock = pg.time.Clock()
        self.menu_items = {
            "new_game": TextItem(0.3175, 0.5, 0.365, "New Game", self.frame, True, 8),
            "options": TextItem(0.37, 0.625, 0.26, "Options", self.frame, True, 8),
            "exit": TextItem(0.4313, 0.75, 0.1375, "Exit", self.frame, True, 8)
        }
        self.title_text = TextItem(0.3, 0.1, 0.7, config.title, self.frame, False, 14)

        self.main_loop()

    def main_loop(self):        
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                elif event.type == pg.MOUSEMOTION:
                    highlighted = -1
                    mouse = pg.mouse.get_pos()
                    for key in self.menu_items.keys():
                        if self.menu_items[key].isHover(mouse):
                            highlighted = key
                    self.draw_game_screen(highlighted)
            
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    click = pg.mouse.get_pressed()

                    if click[0] == 1:
                        for key in self.menu_items.keys():
                            if self.menu_items[key].isHover(mouse):
                                return key

            self.clock.tick(60)
        
        self.quit()

    def draw_game_screen(self, highlighted=-1):
        self.frame.fill(color_dict['black'])
        self.draw_outline()
        self.draw_title()
        self.draw_menu_options(highlighted)
        self.surface.blit(self.frame, (0, 0))
        pg.display.flip()

  
    def draw_outline(self):
        outline = Rect(
            config.border_buffer - config.border_thickness,
            config.border_buffer - config.border_thickness,
            config.board_width + (2 * config.border_thickness),
            config.board_width + (2 * config.border_thickness)
        )
        pg.draw.rect(
            surface=self.frame,
            color=color_dict['off_white'],
            rect=outline,
            width=config.border_thickness
        )
  
    def draw_title(self):
        self.title_text.draw(False)
    
    def draw_menu_options(self, highlighted=-1):
        for key in self.menu_items.keys():
            self.menu_items[key].draw((highlighted == key))

    def quit(self):
        pg.quit()