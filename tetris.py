import sys
import math
import numpy as np
import pygame as pg
from pygame.locals import *

import config
from pause_menu import PauseMenu
from models.tetrominos import Tetrominos
from models.board import Board
from models.current_piece import CurrentPiece
from utils.color_dict import ColorDict

color_dict = ColorDict().colors

class NewGame:
    def __init__(self):
        pg.init()
        pg.display.set_caption(config.title)

        self.draw_time = pg.time.get_ticks()
        self.surface = pg.display.set_mode((config.window['width'], config.window['height']))
        self.tetrominos = Tetrominos()

        self.tetros = self.tetrominos.shapes
        self.tetro_types = self.tetrominos.get_types()

        self.lose = False
        self.win = False
        self.rows_cleared = 0
        self.current_level = 1
        self.score = 0
        self.space_size = 30
        self.board_spaces = [10, 20]

        self.cool_down = config.cool_down
        self.last = pg.time.get_ticks()
        self.key_cool_down = config.key_cool_down
        self.key_last = pg.time.get_ticks()

        self.board = Board(self.space_size, self.board_spaces)
        self.current_piece_board_pos = []

    def main(self):
        # init first piece
        self.current_piece = CurrentPiece()
        self.next_piece = CurrentPiece()

        self.draw_game_screen()
        self.draw_tetro()

        while 1:
            # # check for full rows to eliminate
            num_full_rows = self.board.clear_full_rows()
            self.update_score(num_full_rows)
            now = pg.time.get_ticks()
            if now - self.last >= self.cool_down:

                # redraw borders
                #
                # EVENTUALLY:
                #     instead of redrawing borders every frame, create two
                #     surfaces: first on which to draw static elements (bg,
                #       game borders, static text); second on which to draw
                #       dynamic elements every frame (score, pieces, etc.)
                #
                #

                self.draw_board()
                self.last = now

                if self.is_bottomed():
                    self.on_bottomed()
                else:
                    self.current_piece.increment_pos(1, 1)
                    self.draw_game_screen()
                    self.draw_tetro()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    press = self.get_key_pressed()
                    if press == "left":
                        movement_valid = self.is_valid_shift("left")
                        if movement_valid:
                            self.current_piece.increment_pos(0, -1)
                            self.draw_game_screen()
                            self.draw_tetro()

                    elif press == "right":
                        movement_valid = self.is_valid_shift("right")
                        if movement_valid:
                            self.current_piece.increment_pos(0, 1)
                            self.draw_game_screen()
                            self.draw_tetro()

                    elif press == "down":
                        bottomed = self.is_bottomed()
                        if not bottomed:
                            self.current_piece.increment_pos(1, 1)
                            self.last = now
                            self.draw_game_screen()
                            self.draw_tetro()
                        else:
                            self.on_bottomed()

                    elif press == "rotate":
                        if self.is_valid_rotation():
                            self.current_piece.rotate()
                    
                    elif press == "pause":
                        self.pause_menu()

            pg.display.update()

    def draw_game_screen(self):
        self.draw_background()
        self.draw_board()
        # grid-lines for testing
        # self.draw_empty_grid()
        self.draw_text()
        self.draw_next_tetro()
        pg.display.flip()

    def draw_background(self):
        # fill background with black
        background = pg.Surface(self.surface.get_size())
        background.fill(color_dict['black'])

        # Blit background to the screen
        self.surface.blit(background, (0, 0))

    def draw_board(self):
        m = ((config.window['width'] - self.board.get_board_size()[0]) / 2)
        n = (config.window['height'] - self.board.get_board_size()[1] - 2) + 1

        for y in range(0, 20):
            for x in range(0, 10):
                color = self.board.get()[y][x]['color'] if self.board.get()[y][x]['color'] is not None else (20, 10, 28)
                r = Rect(m + 1, n + 1, self.space_size - 2, self.space_size - 2)
                pg.draw.rect(surface=self.surface, color=color, rect=r)
                m += self.space_size
            n += self.space_size
            m = ((config.window['width'] - self.board.get_board_size()[0]) / 2)

        r = Rect(
            ((config.window['width'] - self.board.get_board_size()[0]) / 2) - 1,
            (config.window['height'] - self.board.get_board_size()[1] - 2),
            self.board.get_board_size()[0] + 2,
            self.board.get_board_size()[1] + 2
        )
        pg.draw.rect(surface=self.surface, color=color_dict['blue'], rect=r, width=1)

    def draw_text(self):
        font = pg.font.SysFont('amiri', 25)
        score_text = font.render(f'Score: {self.score}', True, color_dict['light_blue'], None)
        level_text = font.render(f'Level: {self.get_level()}', True, color_dict['light_blue'], None)
        next_block_text = font.render('Next: ', True, color_dict['light_blue'], None)

        score_text_rect = score_text.get_rect()
        score_text_rect.center = (config.window['width'] * 0.82, config.window['height'] * 0.08)
        level_text_rect = score_text.get_rect()
        level_text_rect.center = (config.window['width'] * 0.82, config.window['height'] * 0.13)
        next_block_text_rect = score_text.get_rect()
        next_block_text_rect.center = (config.window['width'] * 0.82, config.window['height'] * 0.18)

        self.surface.blit(score_text, score_text_rect)
        self.surface.blit(level_text, level_text_rect)
        self.surface.blit(next_block_text, next_block_text_rect)
    
    def draw_empty_grid(self):
        """draw grid for troubleshooting"""
        m = ((config.window['width'] - self.board.get_board_size()[0]) / 2)
        n = (config.window['height'] - self.board.get_board_size()[1] - 2) + 1
        for y in range(0, 20):
            for x in range(0, 10):
                tetro_rect = Rect(m, n, self.space_size, self.space_size)
                pg.draw.rect(surface=self.surface, color=color_dict['grey230'], rect=tetro_rect, width=1)
                m += self.space_size
            n += self.space_size
            m = ((config.window['width'] - self.board.get_board_size()[0]) / 2)

    def draw_tetro(self):
        shape_to_draw = self.current_piece.get_shape()
        piece_pos = self.current_piece.get('pos')
        for i in range(4, -1, -1):
            for j in range(0, 5):
                if shape_to_draw[i][j] == 1:
                    pos = self.board.get_pos_by_coord([piece_pos[0] + j, piece_pos[1] + i])
                    tetro_rect = Rect(pos[0] + 1, pos[1], self.space_size - 2, self.space_size - 2)
                    pg.draw.rect(surface=self.surface, color=self.current_piece.get('color'), rect=tetro_rect)
    
    def draw_next_tetro(self):
        shape_to_draw = self.next_piece.get_shape()
        piece_pos = self.next_piece.get_next_piece_pos()
        for i in range(4, -1, -1):
            for j in range(0, 5):
                if shape_to_draw[i][j] == 1:
                    pos = self.board.get_pos_by_coord([piece_pos[0] + j, piece_pos[1] + i])
                    tetro_rect = Rect(pos[0] + 1, pos[1] + 1, self.space_size - 2, self.space_size - 2)
                    pg.draw.rect(surface=self.surface, color=self.next_piece.get('color'), rect=tetro_rect)

    def get_key_pressed(self):
        now = pg.time.get_ticks()
        if now - self.key_last < self.key_cool_down: return
        pressed_keys = pg.key.get_pressed()
        res = None

        if pressed_keys[K_a] or pressed_keys[K_LEFT]: res = "left"
        elif pressed_keys[K_d] or pressed_keys[K_RIGHT]: res = "right"
        elif pressed_keys[K_s] or pressed_keys[K_DOWN]: res = "down"
        elif pressed_keys[K_SPACE]: res = "rotate"
        elif pressed_keys[K_ESCAPE]: res = "pause"

        if pressed_keys[K_j]: print("swap piece")

        if res is not None: self.key_last = now
        return res

    def is_bottomed(self):
        piece_pos = self.current_piece.get('pos')
        piece_spaces = self.current_piece.get('iterations')[self.current_piece.get('alt')]['points']
        # if space below is occupied
        for pt in piece_spaces:
            if self.board.is_occupied([pt[0] + piece_pos[0], pt[1] + piece_pos[1] + 1]):
                return True
        return False

    def is_valid_shift(self, direction):
        piece_spaces = self.current_piece.get('iterations')[self.current_piece.get('alt')]['points']
        piece_pos = self.current_piece.get('pos')

        if direction == "left":
            for pt in piece_spaces:
                if self.board.is_occupied([pt[0] + piece_pos[0] - 1, pt[1] + piece_pos[1]]): return False
            return True
        
        if direction == "right":
            for pt in piece_spaces:
                if self.board.is_occupied([pt[0] + piece_pos[0] + 1, pt[1] + piece_pos[1]]): return False
            return True
        
        return True

    def is_valid_rotation(self):
        next_alt = (self.current_piece.get('alt') + 1) % len(self.current_piece.get('iterations'))
        piece_pos = self.current_piece.get('pos')
        piece_spaces = self.current_piece.get('iterations')[next_alt]['points']

        for pt in piece_spaces:
            if self.board.is_occupied([pt[0] + piece_pos[0], pt[1] + piece_pos[1]]): return False
        return True
    
    def on_bottomed(self):
        shape = self.current_piece.get_shape()
        for y in range(4, -1, -1):
            for x in range(0, 4):
                if shape[x][y] == 1:
                    self.board.set_board_space_color([self.current_piece.get('pos')[0] + y, self.current_piece.get('pos')[1] + x], self.current_piece.get('color'))

        # set value of current_piece to next_piece & generate next next_piece
        self.current_piece = self.next_piece
        self.next_piece = CurrentPiece()

        # draw new next and current pieces
        self.draw_game_screen()
        self.draw_tetro()


    def update_score(self, val):
        self.score += val
    
    def get_level(self):
        return int(self.score / 10) + 1

    def pause_menu(self):
        pause = PauseMenu(self.surface, self.current_piece.get('color_name')).main()

    def quit(self):
        pg.quit()
