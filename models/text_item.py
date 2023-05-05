import pygame as game
from pygame.locals import *
import config as config
import utils.color_dict as color_dict
import utils.check_pos as pos
color_dict = color_dict.ColorDict().colors

class TextItem:
  def __init__(self, x_rel, y_rel, width_rel, render_text, surface, is_highlightable, size) -> None:
    """
    x_rel: float used to find the x-position of the menu item relative to window size
    y_rel: float used to find the y-position of the menu item relative to window size
    """
    self.surface = surface
    self.is_highlightable = is_highlightable
    self.size = size / 100
    self.font = game.font.SysFont('amiri', round(config.window['height']*self.size))
    self.render = self.font.render(render_text, True, color_dict['off_white'])
    self.highlight_render = self.font.render(render_text, True, color_dict['highlight']) if is_highlightable else None
    self.x_start = round(config.window['width']*x_rel)
    self.y_start = round(config.window['height']*y_rel)
    self.x_end = self.x_start + (config.window['width']*width_rel)
    self.y_end = self.y_start + (config.window['height']*0.1)
    self.render_coords = (self.x_start, self.y_start)
  
  def isHover(self, mouse) -> bool:
    return pos.check_pos(self.x_start, self.x_end, self.y_start, self.y_end, mouse)
  
  def draw(self, highlighted:bool=False) -> None:
    to_draw = self.highlight_render if highlighted else self.render
    self.surface.blit(to_draw, self.render_coords)
