
import sys
import pygame as pg
from pygame.locals import *
import config
from models.text_item import TextItem
import utils.color_dict as color_dict

color_dict = color_dict.ColorDict().colors

class PauseMenu:
    def __init__(self, surface, color):
        pg.display.set_caption(config.title)
        
        self.surface = surface
        # self.menu_items = {}
        self.clock = pg.time.Clock()
        self.color = color
        # self.menu_items = {
        #     "new_game": TextItem(0.3175, 0.5, 0.365, "New Game", self.surface, True, 8),
        #     "options": TextItem(0.37, 0.625, 0.26, "Options", self.surface, True, 8),
        #     "exit": TextItem(0.4313, 0.75, 0.1375, "Exit", self.surface, True, 8)
        # }
        self.title_text = TextItem(0.3, 0.1, 0.7, config.title, self.surface, False, 14)

    def main(self):        
        self.draw_game_screen()
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
                if event.type == pg.KEYDOWN:
                    pressed = pg.key.get_pressed()
                    if pressed[K_ESCAPE]:
                        return

            self.clock.tick(60)
        
        self.quit()

    def draw_game_screen(self, highlighted=-1):
        self.draw_outline()
        self.draw_title()
        self.draw_menu_box()
        # self.draw_menu_options(highlighted)
        self.surface.blit(self.surface, (0, 0))
        pg.display.flip()

  
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
    
    def draw_menu_box(self):
        x, y, w, h = (config.window['width'] * 0.1, config.window['height'] * 0.4, config.window['width'] * 0.8, config.window['height'] * 0.5)
        bg = Rect(x, y, w, h)
        outline = Rect(x + 3, y + 3, w - 6, h - 6)
        inner = Rect(x + 10, y + 10, w - 20, h - 20)
        pg.draw.rect(
            surface=self.surface,
            color=color_dict['grey25'],
            rect=bg
        )
        pg.draw.rect(
            surface=self.surface,
            color=color_dict['grey80'],
            rect=outline,
            width=2
        )
        pg.draw.rect(
            surface=self.surface,
            color=color_dict[f'off_{self.color}'],
            rect=inner
        )
  
    def draw_title(self):
        self.title_text.draw(False)
    
    def draw_menu_options(self, highlighted=-1):
        for key in self.menu_items.keys():
            self.menu_items[key].draw((highlighted == key))
