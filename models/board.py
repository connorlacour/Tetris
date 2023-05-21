from math import floor
import pygame as pg
import config
import copy

class Board:
    def __init__(self, space_size, board_spaces) -> None:
        self.window = config.window
        self.space_size = space_size
        self.board_spaces = board_spaces
        self.drop_grid_spaces = [self.board_spaces[0], 5]
        self.piece_starting_place = [floor((self.board_spaces[0] - 5) / 2), 0]
        self.board = self.generate_board()

    def generate_board(self):
        space = { "color": None }
        return [[ copy.deepcopy(space) for x in range(self.board_spaces[0])] for y in range(self.board_spaces[1])]
    
    def generate_empty_row(self):
        space = { "color": None }
        return [ copy.deepcopy(space) for x in range(self.board_spaces[0])]
    def get_pos_by_coord(self, coord):
        x_offset = (config.window['width'] - self.get_board_size()[0]) / 2
        y_offset = config.window['height'] - self.get_board_size()[1]

        pos_x = x_offset + (coord[0] * self.space_size)
        pos_y = y_offset + (coord[1] * self.space_size)
        return [pos_x, pos_y]

    def get_board_size(self):
        return [self.board_spaces[0] * self.space_size, self.board_spaces[1] * self.space_size]

    def get_drop_grid_size(self):
        return [self.drop_grid_spaces[0] * self.space_size, self.drop_grid_spaces[1] * self.space_size]

    def get(self):
        return self.board
    
    def get_top_of_grid(self):
        return [
            ((config.window['width'] - self.get_board_size()[0]) / 2) + (self.space_size * 2),
            config.window['height'] - self.get_board_size()[1] - (self.space_size * 5)
        ]

    def set_board_space_color(self, coord, color):
        self.board[coord[1]][coord[0]]['color'] = color
    
    def is_occupied(self, pos):
        if (pos[1] < 0): return False
        if (pos[0] < 0 or pos[0] > (self.board_spaces[0] - 1) or pos[1] > (self.board_spaces[1] - 1)): 
            return True
        return self.board[pos[1]][pos[0]]['color'] != None
    
    def clear_full_rows(self):
        full_rows = []
        for row in range(0, 20):
            is_full = True
            for space in self.board[row]:
                if space['color'] is None:
                    is_full = False
            if is_full: full_rows.append(row)
        for idx in full_rows:
            self.board[idx] = self.generate_empty_row()
            for to_shift_idx in range(idx - 1, -1, -1):
                self.board[to_shift_idx + 1] = self.board[to_shift_idx]