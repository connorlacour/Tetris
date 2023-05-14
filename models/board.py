import pygame as pg

class Board:
    def __init__(self, width=10, height=20) -> None:
        self.w = width
        self.h = height
    
    def generate_board(self):
        space = { "color": None }
        return [[space for x in range(self.w)] for y in range(self.h)]

    def generate_board_colors(self):
        return [['X' for x in range(self.w)] for y in range(self.h)]