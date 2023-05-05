import sys
import math
import numpy as np
import pygame as pg
from pygame.locals import *

import config
from models.tetrominos import Tetrominos
from utils.color_dict import ColorDict

color_dict = ColorDict().colors


def generate_board():
    w = 10
    h = 20
    grid_occupied = [[0 for x in range(w)] for y in range(h)]
    return grid_occupied


def generate_board_colors():
    w = 10
    h = 20
    grid_colors = [['X' for x in range(w)] for y in range(h)]
    return grid_colors

class NewGame:
    def __init__(self):
        """
        """
        self.draw_time = pg.time.get_ticks()
        self.window_height = 600
        self.surface = pg.display.set_mode((600, 600))
        self.lose = False
        self.win = False
        self.current_piece = None
        self.tetro_array = ["S", "Z", "J", "L", "I", "O", "T"]

        self.rows_cleared = 0
        self.current_level = 1
        self.score = 0

        self.last = pg.time.get_ticks()
        self.cool_down = 400

        self.key_cool_down = 175
        self.key_last = pg.time.get_ticks()

        self.grid_occupied = generate_board()
        self.grid_colored = generate_board_colors()
        self.current_piece_board_spaces = []

        self.main()

    def main(self):
        # initialize basic screen components
        pg.init()
        pg.display.set_caption(config.title)

        player_lost = False
        first_piece = True
        starting_position = True

        # fill background with off-white
        background = pg.Surface(self.surface.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # Blit background to the screen
        self.surface.blit(background, (0, 0))
        pg.display.flip()

        self.game_screen()

        tetro_shapes = Tetrominos().shapes
        current_piece = self.generate_next_piece()
        alt = 0

        next_piece = self.generate_next_piece()

        cur_x = 275
        cur_y = 98
        next_x = 500
        next_y = 150

        # self.draw_tetro(next_piece, alt, tetro_shapes, next_x, next_y)
        # self.current_piece_occupying(current_piece, alt, tetro_shapes,
        #                              cur_x, cur_y)

        self.gameplay_text()

        # final row: self.grid_occupied[19][i] = 1

        moved_left = False
        moved_right = False

        # while game is not quit
        while 1:
            if starting_position:
                self.draw_tetro(current_piece, alt, tetro_shapes,
                                cur_x, cur_y)
                starting_position = False

            else:
                # # check for full rows
                # self.rows_check()
                self.key_press()

                now = pg.time.get_ticks()
                # print("now: " + str(now))
                # print("last: " + str(self.last))

                # if the appropriate amount of time has passed, move tetro
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
                    self.game_screen()

                    self.last = now

                    # draw tetro if it has not bottomed out
                    # if not self.has_bottomed():
                    #     # "clear" previous drawing of falling tetro
                    #     self.reset_for_moving_piece(current_piece, alt,
                    #                                 tetro_shapes,
                    #                                 cur_x, cur_y)
                    #     # increment cur_y
                    #     cur_y += 25
                    #     self.draw_tetro(current_piece, alt,
                    #                     tetro_shapes, cur_x, cur_y)
                    #     self.current_piece_occupying(current_piece, alt,
                    #                                  tetro_shapes,
                    #                                  cur_x, cur_y)
                    #     # self.has_bottomed()

                    # if self.has_bottomed():
                    #     self.current_piece_occupying(current_piece, alt,
                    #                                  tetro_shapes, cur_x, cur_y)

                    #     # mark resting place of piece in grid_occupied
                    #     self.update_grid_occupied()
                    #     self.update_grid_colors(
                    #         self.current_piece_board_spaces,
                    #         current_piece, tetro_shapes)

                    #     # reset cur_x and cur_y to top of board
                    #     # reset alt to default 0
                    #     cur_x = 275
                    #     cur_y = 98
                    #     alt = 0

                    #     # set value of current_piece to next_piece
                    #     current_piece = next_piece

                    #     # clear drawing of next_piece to allow for next
                    #     # next_piece
                    #     self.reset_for_moving_piece(next_piece, alt,
                    #                                 tetro_shapes,
                    #                                 next_x, next_y)

                    #     # generate next_piece
                    #     next_piece = self.generate_next_piece()

                    #     # reset current_piece_occupying values to new
                    #     # current_piece
                    #     self.current_piece_occupying(current_piece, alt,
                    #                                  tetro_shapes,
                    #                                  cur_x, cur_y)

                    #     # draw new next and current pieces
                    #     self.draw_tetro(current_piece, alt, tetro_shapes,
                    #                     cur_x, cur_y)
                    #     self.draw_tetro(next_piece, alt, tetro_shapes,
                    #                     next_x, next_y)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    press = self.key_press()
                    if press == "left":
                        movement_valid = self.valid_shift("left")
                        if movement_valid:
                            cur_x -= 25
                            self.reset_for_moving_piece(current_piece, alt,
                                                        tetro_shapes,
                                                        cur_x+25, cur_y)
                            self.draw_tetro(current_piece, alt, tetro_shapes,
                                            cur_x, cur_y)

                    elif press == "right":
                        movement_valid = self.valid_shift("right")
                        if movement_valid:
                            cur_x += 25
                            self.reset_for_moving_piece(current_piece, alt,
                                                        tetro_shapes,
                                                        cur_x-25, cur_y)
                            self.draw_tetro(current_piece, alt, tetro_shapes,
                                            cur_x, cur_y)

                    elif press == "down":
                        bottomed = self.has_bottomed()
                        if not bottomed:
                            cur_y += 25
                            self.last = now
                            self.reset_for_moving_piece(current_piece, alt,
                                                        tetro_shapes,
                                                        cur_x, cur_y-25)
                            self.draw_tetro(current_piece, alt, tetro_shapes,
                                            cur_x, cur_y)

                    elif press == "rotate":
                        is_valid = self.valid_rotation(current_piece, alt,
                                                       tetro_shapes)

                        if is_valid >= 0:

                            print('position before: ' +
                                  str(self.current_piece_board_spaces))

                            old_alt = alt
                            alt = is_valid
                            # print('alt: ' + str(alt))

                            self.reset_for_moving_piece(current_piece, old_alt,
                                                        tetro_shapes,
                                                        cur_x, cur_y)
                            self.draw_tetro(current_piece, alt, tetro_shapes,
                                            cur_x, cur_y)

                            self.current_piece_occupying(current_piece,
                                                         alt, tetro_shapes,
                                                         cur_x, cur_y)


                            print('position after: ' +
                                  str(self.current_piece_board_spaces))

                        else:
                            print('is valid result was: ' + str(is_valid))

                    self.current_piece_occupying(current_piece, alt,
                                                 tetro_shapes,
                                                 cur_x, cur_y)

            pg.display.update()

    # # write main_menu()
    # def main_menu(self):
    #     pass

    # # write pause_menu()
    # def pause_menu(self):
    #     pass

    # # move main() functions running tetris here
    # def run_tetris(self):
    #     pass

    def game_screen(self):
        sizer = 25
        total_width = self.window_height

        game_x = 10 * sizer
        game_y = 20 * sizer
        r = Rect(((total_width - game_x) / 2)-1, (total_width - game_y - 3),
                 game_x + 2, game_y+3)

        pg.draw.rect(surface=self.surface, color=color_dict['blue'], rect=r, width=1)

    def gameplay_text(self):
        current_level = 1
        current_score = 69

        font = pg.font.SysFont('arial', 25)
        score_text = font.render('Score:   ' + str(self.score), True,
                                 color_dict['light_blue'], None)
        level_text = font.render('Level:   ' + str(self.current_level), True,
                                 color_dict['light_blue'], None)
        next_block_text = font.render('Next: ', True, color_dict['light_blue'], None)

        score_text_rect = score_text.get_rect()
        score_text_rect.center = (490, 50)
        level_text_rect = score_text.get_rect()
        level_text_rect.center = (490, 80)
        next_block_text_rect = score_text.get_rect()
        next_block_text_rect.center = (520, 110)

        self.surface.blit(score_text, score_text_rect)
        self.surface.blit(level_text, level_text_rect)
        self.surface.blit(next_block_text, next_block_text_rect)

    def draw_tetro(self, tetro_type, alt, shapes, cur_x, cur_y):
        shape_to_print = shapes[tetro_type]['iterations'][alt]['shape']
        shape_color = shapes[tetro_type]['color']

        first_drawn = True
        first_drawn_x = None
        first_drawn_y = None

        m = 175
        n = 100

        # draw top row slots for troubleshooting
        #
        #
        for x in range(0, 10):
        
            tetro_rect = Rect(m, n, 25, 25)
            pg.draw.rect(surface=self.surface, color=color_dict['grey230'],
                           rect=tetro_rect, width=1)
            m += 25

        for i in range(0, 5):
            for j in range(0, 5):
                if shape_to_print[i][j] == 1:

                    if first_drawn:

                        x_pos_draw = cur_x
                        y_pos_draw = cur_y
                        first_drawn_x = j
                        first_drawn_y = i

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        pg.draw.rect(surface=self.surface, color=shape_color,
                                       rect=tetro_rect)
                        pg.draw.rect(surface=self.surface, color=color_dict['grey230'],
                                       rect=tetro_rect, width=1)
                        first_drawn = False
                    else:
                        x_pos_draw = cur_x + ((j-first_drawn_x) * 25)
                        y_pos_draw = cur_y + ((i-first_drawn_y) * 25)

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        pg.draw.rect(surface=self.surface, color=shape_color,
                                       rect=tetro_rect)
                        pg.draw.rect(surface=self.surface, color=color_dict['grey230'],
                                       rect=tetro_rect, width=1)

    def generate_next_piece(self):
        next_piece = np.random.choice(self.tetro_array)
        print('next piece, from random.. ', next_piece)
        return next_piece

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

    # def current_piece_occupying(self, tetro_type, alt, shapes, cur_x, cur_y):
    #     shape_to_print = shapes[tetro_type]['shape']

    #     self.current_piece_board_spaces = []
    #     grid_x = int((cur_x - 175) / 25)
    #     grid_y = int((cur_y - 97) / 25)
    #     # print('grid x: ' + str(grid_x))
    #     # print('grid y: ' + str(grid_y))

    #     y_offset = 0
    #     first_val = True
    #     for i in range(0, 5):
    #         for j in range(0, 5):
    #             if shape_to_print[i][j] == 1:
    #                 if first_val:
    #                     y_offset = i
    #                     x_offset = j
    #                     self.current_piece_board_spaces.append([grid_x,
    #                                                             grid_y])
    #                     first_val = False
    #                 else:
    #                     self.current_piece_board_spaces.append(
    #                         [(grid_x + j - x_offset),
    #                          (grid_y + i - y_offset)])

    def has_bottomed(self):
        for i in range(0, 4):
            if self.current_piece_board_spaces[i][1] == 19:
                return True
            else:
                piece_val_y = self.current_piece_board_spaces[i][1]
                piece_val_x = self.current_piece_board_spaces[i][0]
                if self.grid_occupied[piece_val_y + 1][piece_val_x] == 1:
                    return True
        return False

    # def update_grid_occupied(self):
    #     for i in range(0, 4):
    #         piece_val_x = self.current_piece_board_spaces[i][0]
    #         piece_val_y = self.current_piece_board_spaces[i][1]
    #         self.grid_occupied[piece_val_y][piece_val_x] = 1

    def key_press(self):
        now = pg.time.get_ticks()
        key_pressed = False
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

    # def valid_shift(self, direction):
    #     if direction == "left":
    #         for i in range(0, 4):
    #             if self.current_piece_board_spaces[i][0] == 0:
    #                 return False
    #             piece_x_val = self.current_piece_board_spaces[i][0]
    #             piece_y_val = self.current_piece_board_spaces[i][1]
    #             if self.grid_occupied[piece_y_val][piece_x_val-1] == 1:
    #                 print('left occupied')
    #                 return False
    #         return True
    #     if direction == "right":
    #         for j in range(0, 4):
    #             if self.current_piece_board_spaces[j][0] == 9:
    #                 return False
    #             piece_x_val = self.current_piece_board_spaces[j][0]
    #             piece_y_val = self.current_piece_board_spaces[j][1]
    #             if self.grid_occupied[piece_y_val][piece_x_val+1] == 1:
    #                 print('right occupied')
    #                 return False
    #         return True

    def update_grid_colors(self, tetro_array, tetro_type, shapes):
        shape_color = shapes[tetro_type]['color']
        for a in tetro_array:
            self.grid_colored[a[1]][a[0]] = shape_color
        print('color was ' + str(shape_color))
        print('new colored grid: ' + str(self.grid_colored))

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
    #             if self.grid_occupied[i][j] == 1:
    #                 count += 1

    #         if count == 10:
    #             self.clear_full_row(i)


    def clear_full_row(self, row):
        pass

    def update_score(self):
        pass
