import sys
import math
import numpy as np
import pygame as pg
from pygame.locals import *

import config
from models.tetrominos import Tetrominos
from models.board import Board
from models.current_piece import CurrentPiece
from utils.color_dict import ColorDict

color_dict = ColorDict().colors

class NewGame:
    def __init__(self):
        
        # initialize basic screen components
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
        self.score = 69
        self.space_size = 30
        self.board_spaces = [10, 20]

        self.cool_down = config.cool_down
        self.last = pg.time.get_ticks()
        self.key_cool_down = config.key_cool_down
        self.key_last = pg.time.get_ticks()

        self.board = Board(self.space_size, self.board_spaces)
        self.current_piece_board_pos = []

        self.main()

    def main(self):
        # init first piece
        self.current_piece = CurrentPiece()
        self.next_piece = CurrentPiece()

        self.draw_game_screen()
        self.draw_tetro(self.current_piece.get())

        while 1:
            # # check for full rows to eliminate
            # self.rows_check()
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

                # increment and draw tetro if it has not bottomed out
                if not self.has_bottomed():
                    self.current_piece.increment_pos(1, 1)
                    self.draw_game_screen()
                    self.draw_tetro(self.current_piece.get())
                    # self.current_piece_occupying(current_piece, self.tetros, cur_x, cur_y)
                    # self.has_bottomed()

                # if self.has_bottomed():
                #     self.current_piece_occupying(current_piece, alt, self.tetros, cur_x, cur_y)

                #     # mark resting place of piece in board
                #     self.update_board()
                #     self.update_board_colors(self.current_piece_board_pos, current_piece, self.tetros)

                #     # reset cur_x and cur_y to top of board
                #     # reset alt to default 0
                #     cur_x = 275
                #     cur_y = 98
                #     alt = 0

                #     # set value of current_piece to next_piece
                #     current_piece = next_piece

                #     # clear drawing of next_piece to allow for next
                #     # next_piece
                #     self.reset_for_moving_piece(next_piece, alt, self.tetros, next_x, next_y)

                #     # generate next_piece
                #     next_piece = self.generate_next_piece()

                #     # reset current_piece_occupying values to new
                #     # current_piece
                #     self.current_piece_occupying(current_piece, alt, self.tetros, cur_x, cur_y)

                #     # draw new next and current pieces
                #     self.draw_tetro(current_piece)
                #     self.draw_tetro(next_piece)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    press = self.get_key_pressed()
                    if press == "left":
                        movement_valid = self.valid_shift("left")
                        if movement_valid:
                            self.current_piece.increment_pos(0, -1)
                            self.draw_game_screen()
                            self.draw_tetro(self.current_piece.get())

                    elif press == "right":
                        movement_valid = self.valid_shift("right")
                        if movement_valid:
                            self.current_piece.increment_pos(0, 1)
                            self.draw_game_screen()
                            self.draw_tetro(self.current_piece.get())

                    elif press == "down":
                        bottomed = self.has_bottomed()
                        if not bottomed:
                            self.current_piece.increment_pos(1, 1)
                            self.last = now
                            self.draw_game_screen()
                            self.draw_tetro(self.current_piece.get())

                    elif press == "rotate":
                        print('rotate..')
                        # is_valid = self.valid_rotation(current_piece,  self.tetros)

                        # if is_valid >= 0:

                        #     print('position before: ' + str(self.current_piece_board_pos))

                        #     old_alt = alt
                        #     alt = is_valid

                        #     # self.reset_for_moving_piece(current_piece, old_alt, self.tetros, cur_x, cur_y)
                        #     self.draw_tetro(current_piece)

                        #     # self.current_piece_occupying(current_piece, alt, self.tetros, cur_x, cur_y)


                        #     print('position after: ' + str(self.current_piece_board_pos))

                        # else:
                        #     print('is valid result was: ' + str(is_valid))

                    # self.current_piece_occupying(current_piece, alt, self.tetros, cur_x, cur_y)

            pg.display.update()

    def draw_game_screen(self):
        self.draw_background()
        self.draw_board()
        # grid-lines for testing
        self.draw_empty_grid()
        self.draw_text()
        pg.display.flip()

    def draw_background(self):
        # fill background with black
        background = pg.Surface(self.surface.get_size())
        background.fill(color_dict['black'])

        # Blit background to the screen
        self.surface.blit(background, (0, 0))

    def draw_board(self):
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
        level_text = font.render(f'Level: {self.current_level}', True, color_dict['light_blue'], None)
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

    def draw_tetro(self, tetro):
        shape_to_draw = tetro['iterations'][tetro['alt']]['shape']
        for i in range(0, 5):
            for j in range(0, 5):
                if shape_to_draw[i][j] == 1:
                    pos = self.board.get_pos_by_coord([tetro['pos'][0] + j, tetro['pos'][1] + i])
                    tetro_rect = Rect(pos[0], pos[1], self.space_size, self.space_size)
                    pg.draw.rect(surface=self.surface, color=tetro['color'], rect=tetro_rect)

    # def reset_for_moving_piece(self, tetro_type, alt, shapes, cur_x, cur_y):
    
    #     if alt == 0:
    #         shape_to_print = shapes[tetro_type]['shape']
    #     elif alt == 1:
    #         shape_to_print = shapes[tetro_type]['alt1']
    #     elif alt == 2:
    #         shape_to_print = shapes[tetro_type]['alt2']
    #     elif alt == 3:
    #         shape_to_print = shapes[tetro_type]['alt3']

    #     first_drawn = True
    #     first_drawn_x = None
    #     first_drawn_y = None
    #     for i in range(0, 5):
    #         for j in range(0, 5):
    #             if shape_to_print[i][j] == 1:

    #                 if first_drawn:

    #                     x_pos_draw = cur_x
    #                     y_pos_draw = cur_y
    #                     first_drawn_x = j
    #                     first_drawn_y = i

    #                     tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
    #                     pg.draw.rect(surface=self.surface, color=black,
    #                                    rect=tetro_rect)
    #                     first_drawn = False
    #                 else:
    #                     x_pos_draw = cur_x + ((j - first_drawn_x) * 25)
    #                     y_pos_draw = cur_y + ((i - first_drawn_y) * 25)

    #                     tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
    #                     pg.draw.rect(surface=self.surface, color=black,
    #                                    rect=tetro_rect)

    # def current_piece_occupying(self, tetro_type, shapes, cur_x, cur_y):
    #     shape_to_print = shapes[tetro_type]['shape']

    #     self.current_piece_board_pos = []
    #     board_size[0] = int((cur_x - 175) / 25)
    #     board_size[1] = int((cur_y - 97) / 25)
    #     # print('grid x: ' + str(board_size[0]))
    #     # print('grid y: ' + str(board_size[1]))

    #     y_offset = 0
    #     first_val = True
    #     for i in range(0, 5):
    #         for j in range(0, 5):
    #             if shape_to_print[i][j] == 1:
    #                 if first_val:
    #                     y_offset = i
    #                     x_offset = j
    #                     self.current_piece_board_pos.append([board_size[0],
    #                                                             board_size[1]])
    #                     first_val = False
    #                 else:
    #                     self.current_piece_board_pos.append(
    #                         [(board_size[0] + j - x_offset),
    #                          (board_size[1] + i - y_offset)])

    def has_bottomed(self):
        print('CUR POS')
        print(self.current_piece.get()['pos'])
        # for bottom row
        shape = self.current_piece.get_shape()
        lowest_occupied_row = 4 if (1 in shape[4]) else 3 if (1 in shape[3]) else 2
        for i in range(0, 5):
            print(shape[0][i])
            if shape[lowest_occupied_row][i] == 19:
                return True
            # else:
            #     piece_val_y = self.current_piece_board_pos[i][1]
            #     piece_val_x = self.current_piece_board_pos[i][0]
            #     if self.board[piece_val_y + 1][piece_val_x] == 1:
            #         return True
        return False

    # def update_board(self):
    #     for i in range(0, 4):
    #         piece_val_x = self.current_piece_board_pos[i][0]
    #         piece_val_y = self.current_piece_board_pos[i][1]
    #         self.board[piece_val_y][piece_val_x] = 1

    def update_board_colors(self, tetro_types, tetro_type, shapes):
        for a in tetro_types:
            self.board.get_board()[a[1]][a[0]] = shapes[tetro_type]['color']
        # print('color was ' + str(shapes[tetro_type]['color']))
        # print('new colored grid: ' + str(self.board))

    def get_key_pressed(self):
        now = pg.time.get_ticks()
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[K_a]:
            if now - self.key_last >= self.key_cool_down:
                self.key_last = now
                print('moving left')
                return "left"
        elif pressed_keys[K_d]:
            if now - self.key_last >= self.key_cool_down:
                self.key_last = now
                print('moving right')
                return "right"
        if pressed_keys[K_s]:
            if now - self.key_last >= self.key_cool_down:
                self.key_last = now
                print('moving down faster')
                return "down"
        if pressed_keys[K_SPACE]:
            if now - self.key_last >= self.key_cool_down:
                self.key_last = now
                print('rotating')
                return "rotate"

        if pressed_keys[K_j]:
            print("swap piece")

    def valid_shift(self, direction):
        piece_spaces = self.current_piece.get()['iterations'][self.current_piece.get()['alt']]['points']
        piece_pos = self.current_piece.get()['pos']
        if direction == "left":
            for pt in piece_spaces:
                if self.board.is_occupied([pt[0] + piece_pos[0], pt[1] + piece_pos[1]]):
                    print('left occupied')
                    return False
            return True
        # if direction == "right":
        #     for j in range(0, 4):
        #         if self.current_piece_board_pos[j][0] == 9:
        #             return False
        #         piece_x_val = self.current_piece_board_pos[j][0]
        #         piece_y_val = self.current_piece_board_pos[j][1]
        #         if self.board.get_board()[piece_y_val][piece_x_val+1] == 1:
        #             print('right occupied')
        #             return False
        #     return True
        return True

    # def valid_rotation(self, tetro_type, alt, shapes):
    #     if alt == 0:
    #         if 'alt1' in shapes[tetro_type]:
    #             return 1
    #     elif alt == 1:
    #         if 'alt2' in shapes[tetro_type]:
    #             return 2
    #         else:
    #             return 0
    #     elif alt == 2:
    #         return 3
    #     else:
    #         print("cannot rotate")
    #         return 0
    #     return -1

    # def rows_check(self):
    #     for i in range(0, 20):
    #         count = 0
    #         for j in range(0, 10):
    #             if self.board.get_board()[i][j] == 1:
    #                 count += 1

    #         if count == 10:
    #             self.clear_full_row(i)


    def clear_full_row(self, row):
        pass

    def update_score(self):
        pass

    def pause_menu(self):
        pass

    def quit(self):
        pg.quit()
