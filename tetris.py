import sys
import math
import numpy as np
import pygame as game
from pygame.locals import *


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


def generate_tetro_shapes():

    purple = (136, 0, 204)
    green = (25, 255, 140)
    yellow = (255, 255, 51)
    red = (255, 51, 51)
    blue = (64, 25, 255)
    light_blue = (25, 255, 255)
    orange = (255, 153, 51)

    w = 5
    h = 5

    o_coords = [[2, 1], [2, 2], [3, 1], [3, 2]]

    i_coords = [[0, 2], [1, 2], [2, 2], [3, 2]]
    i_coords_alt_1 = [[2, 0], [2, 1], [2, 2], [2, 3]]

    j_coords = [[1, 1], [2, 1], [2, 2], [2, 3]]
    j_coords_alt_1 = [[1, 2], [1, 3], [2, 2], [3, 2]]
    j_coords_alt_2 = [[2, 1], [2, 2], [2, 3], [3, 3]]
    j_coords_alt_3 = [[1, 2], [2, 2], [3, 1], [3, 2]]

    l_coords = [[1, 3], [2, 1], [2, 2], [2, 3]]
    l_coords_alt_1 = [[1, 2], [2, 2], [3, 2], [3, 3]]
    l_coords_alt_2 = [[2, 1], [2, 2], [2, 3], [3, 1]]
    l_coords_alt_3 = [[1, 1], [1, 2], [2, 2], [3, 2]]

    z_coords = [[2, 1], [2, 2], [3, 2], [3, 3]]
    z_coords_alt_1 = [[1, 2], [2, 1], [2, 2], [3, 1]]

    s_coords = [[2, 2], [2, 3], [3, 1], [3, 2]]
    s_coords_alt_1 = [[1, 2], [2, 2], [2, 3], [3, 3]]

    t_coords = [[1, 2], [2, 1], [2, 2], [2, 3]]
    t_coords_alt_1 = [[1, 2], [2, 2], [2, 3], [3, 2]]
    t_coords_alt_2 = [[2, 1], [2, 2], [2, 3], [3, 2]]
    t_coords_alt_3 = [[1, 2], [2, 2], [2, 1], [3, 2]]

    # print(blank_shape)

    o_shape = [[0 for x in range(w)] for y in range(h)]

    s_shape = [[0 for x in range(w)] for y in range(h)]
    s_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]

    z_shape = [[0 for x in range(w)] for y in range(h)]
    z_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]

    i_shape = [[0 for x in range(w)] for y in range(h)]
    i_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]

    j_shape = [[0 for x in range(w)] for y in range(h)]
    j_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]
    j_shape_alt_2 = [[0 for x in range(w)] for y in range(h)]
    j_shape_alt_3 = [[0 for x in range(w)] for y in range(h)]

    l_shape = [[0 for x in range(w)] for y in range(h)]
    l_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]
    l_shape_alt_2 = [[0 for x in range(w)] for y in range(h)]
    l_shape_alt_3 = [[0 for x in range(w)] for y in range(h)]

    t_shape = [[0 for x in range(w)] for y in range(h)]
    t_shape_alt_1 = [[0 for x in range(w)] for y in range(h)]
    t_shape_alt_2 = [[0 for x in range(w)] for y in range(h)]
    t_shape_alt_3 = [[0 for x in range(w)] for y in range(h)]

    for coord in o_coords:
        o_shape[coord[0]][coord[1]] = 1

    # generate T shapes
    for coord in t_coords:
        t_shape[coord[0]][coord[1]] = 1
    for coord in t_coords_alt_1:
        t_shape_alt_1[coord[0]][coord[1]] = 1
    for coord in t_coords_alt_2:
        t_shape_alt_2[coord[0]][coord[1]] = 1
    for coord in t_coords_alt_3:
        t_shape_alt_3[coord[0]][coord[1]] = 1

    # generate S shapes
    for coord in s_coords:
        s_shape[coord[0]][coord[1]] = 1
    for coord in s_coords_alt_1:
        s_shape_alt_1[coord[0]][coord[1]] = 1

    # generate Z shapes
    for coord in z_coords:
        z_shape[coord[0]][coord[1]] = 1
    for coord in z_coords_alt_1:
        z_shape_alt_1[coord[0]][coord[1]] = 1

    # generate I shapes
    for coord in i_coords:
        i_shape[coord[0]][coord[1]] = 1
    for coord in i_coords_alt_1:
        i_shape_alt_1[coord[0]][coord[1]] = 1

    # generate J shapes
    for coord in j_coords:
        j_shape[coord[0]][coord[1]] = 1
    for coord in j_coords_alt_1:
        j_shape_alt_1[coord[0]][coord[1]] = 1
    for coord in j_coords_alt_2:
        j_shape_alt_2[coord[0]][coord[1]] = 1
    for coord in j_coords_alt_3:
        j_shape_alt_3[coord[0]][coord[1]] = 1

    for coord in l_coords:
        l_shape[coord[0]][coord[1]] = 1
    for coord in l_coords_alt_1:
        l_shape_alt_1[coord[0]][coord[1]] = 1
    for coord in l_coords_alt_2:
        l_shape_alt_2[coord[0]][coord[1]] = 1
    for coord in l_coords_alt_3:
        l_shape_alt_3[coord[0]][coord[1]] = 1

    updated_shapes = {'T': {'shape': t_shape, 'color': purple,
                            'alt1': t_shape_alt_1, 'alt2': t_shape_alt_2,
                            'alt3': t_shape_alt_3},

                      'S': {'shape': s_shape, 'color': green,
                            'alt1': s_shape_alt_1},

                      'O': {'shape': o_shape, 'color': yellow},

                      'Z': {'shape': z_shape, 'color': red,
                            'alt1': z_shape_alt_1},

                      'J': {'shape': j_shape, 'color': blue,
                            'alt1': j_shape_alt_1, 'alt2': j_shape_alt_2,
                            'alt3': j_shape_alt_3},

                      'L': {'shape': l_shape, 'color': orange,
                            'alt1': l_shape_alt_1, 'alt2': l_shape_alt_2,
                            'alt3': l_shape_alt_3
                            },

                      'I': {'shape': i_shape, 'color': light_blue,
                            'alt1': i_shape_alt_1}}

    return updated_shapes


class Window:
    def __init__(self):
        """
        """
        self.draw_time = game.time.get_ticks()
        self.window_height = 600
        self.surface = game.display.set_mode((600, 600))
        self.lose = False
        self.win = False
        self.current_piece = None
        self.tetro_array = ["S", "Z", "J", "L", "I", "O", "T"]

        self.rows_cleared = 0
        self.current_level = 1
        self.score = 0

        self.last = game.time.get_ticks()
        self.cool_down = 400

        self.key_cool_down = 175
        self.key_last = game.time.get_ticks()

        self.grid_occupied = generate_board()
        self.grid_colored = generate_board_colors()
        self.current_piece_board_spaces = []

        self.main()

    def main(self):
        # initialize basic screen components
        game.init()
        game.display.set_caption('Tetris')

        player_lost = False
        first_piece = True
        starting_position = True

        # fill background with off-white
        background = game.Surface(self.surface.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # Blit background to the screen
        self.surface.blit(background, (0, 0))
        game.display.flip()

        self.game_screen()

        tetro_shapes = generate_tetro_shapes()
        current_piece = self.generate_next_piece()
        alt = 0

        next_piece = self.generate_next_piece()

        cur_x = 275
        cur_y = 98
        next_x = 500
        next_y = 150

        self.draw_tetro(next_piece, alt, tetro_shapes, next_x, next_y)
        self.current_piece_occupying(current_piece, alt, tetro_shapes,
                                     cur_x, cur_y)

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
                # check for full rows
                self.rows_check()

                self.key_press()

                now = game.time.get_ticks()
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
                    if not self.has_bottomed():
                        # "clear" previous drawing of falling tetro
                        self.reset_for_moving_piece(current_piece, alt,
                                                    tetro_shapes,
                                                    cur_x, cur_y)
                        # increment cur_y
                        cur_y += 25
                        self.draw_tetro(current_piece, alt,
                                        tetro_shapes, cur_x, cur_y)
                        self.current_piece_occupying(current_piece, alt,
                                                     tetro_shapes,
                                                     cur_x, cur_y)
                        self.has_bottomed()

                    if self.has_bottomed():
                        self.current_piece_occupying(current_piece, alt,
                                                     tetro_shapes, cur_x, cur_y)

                        # mark resting place of piece in grid_occupied
                        self.update_grid_occupied()
                        self.update_grid_colors(
                            self.current_piece_board_spaces,
                            current_piece, tetro_shapes)

                        # reset cur_x and cur_y to top of board
                        # reset alt to default 0
                        cur_x = 275
                        cur_y = 98
                        alt = 0

                        # set value of current_piece to next_piece
                        current_piece = next_piece

                        # clear drawing of next_piece to allow for next
                        # next_piece
                        self.reset_for_moving_piece(next_piece, alt,
                                                    tetro_shapes,
                                                    next_x, next_y)

                        # generate next_piece
                        next_piece = self.generate_next_piece()

                        # reset current_piece_occupying values to new
                        # current_piece
                        self.current_piece_occupying(current_piece, alt,
                                                     tetro_shapes,
                                                     cur_x, cur_y)

                        # draw new next and current pieces
                        self.draw_tetro(current_piece, alt, tetro_shapes,
                                        cur_x, cur_y)
                        self.draw_tetro(next_piece, alt, tetro_shapes,
                                        next_x, next_y)

            for event in game.event.get():
                if event.type == game.KEYDOWN:
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

            game.display.update()

    # write main_menu()
    def main_menu(self):
        pass

    # write pause_menu()
    def pause_menu(self):
        pass

    # move main() functions running tetris here
    def run_tetris(self):
        pass

    def game_screen(self):
        blue = (50, 20, 250)
        sizer = 25
        total_width = self.window_height

        game_x = 10 * sizer
        game_y = 20 * sizer
        r = Rect(((total_width - game_x) / 2)-1, (total_width - game_y - 3),
                 game_x + 2, game_y+3)

        game.draw.rect(surface=self.surface, color=blue, rect=r, width=1)

    def gameplay_text(self):
        light_blue = (220, 220, 250)
        # print(game.font.get_fonts())
        current_level = 1
        current_score = 69
        font = game.font.SysFont('arial', 25)
        score_text = font.render('Score:   ' + str(self.score), True,
                                 light_blue, None)
        level_text = font.render('Level:   ' + str(self.current_level), True,
                                 light_blue, None)
        next_block_text = font.render('Next: ', True, light_blue, None)

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

        grey = (230, 230, 230)

        if alt == 0:
            shape_to_print = shapes[tetro_type]['shape']
        elif alt == 1:
            shape_to_print = shapes[tetro_type]['alt1']
        elif alt == 2:
            shape_to_print = shapes[tetro_type]['alt2']
        elif alt == 3:
            shape_to_print = shapes[tetro_type]['alt3']
        shape_color = shapes[tetro_type]['color']

        first_drawn = True
        first_drawn_x = None
        first_drawn_y = None

        m = 175
        n = 100

        # draw top row slots for troubleshooting
        #
        #
        # for x in range(0, 10):
        #
        #     tetro_rect = Rect(m, n, 25, 25)
        #     game.draw.rect(surface=self.surface, color=grey,
        #                    rect=tetro_rect, width=1)
        #     m += 25

        for i in range(0, 5):
            for j in range(0, 5):
                if shape_to_print[i][j] == 1:

                    if first_drawn:

                        x_pos_draw = cur_x
                        y_pos_draw = cur_y
                        first_drawn_x = j
                        first_drawn_y = i

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        game.draw.rect(surface=self.surface, color=shape_color,
                                       rect=tetro_rect)
                        game.draw.rect(surface=self.surface, color=grey,
                                       rect=tetro_rect, width=1)
                        first_drawn = False
                    else:
                        x_pos_draw = cur_x + ((j-first_drawn_x) * 25)
                        y_pos_draw = cur_y + ((i-first_drawn_y) * 25)

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        game.draw.rect(surface=self.surface, color=shape_color,
                                       rect=tetro_rect)
                        game.draw.rect(surface=self.surface, color=grey,
                                       rect=tetro_rect, width=1)

    def generate_next_piece(self):
        next_piece = np.random.choice(self.tetro_array)
        return next_piece

    def reset_for_moving_piece(self, tetro_type, alt, shapes, cur_x, cur_y):
        black = (0, 0, 0)

        if alt == 0:
            shape_to_print = shapes[tetro_type]['shape']
        elif alt == 1:
            shape_to_print = shapes[tetro_type]['alt1']
        elif alt == 2:
            shape_to_print = shapes[tetro_type]['alt2']
        elif alt == 3:
            shape_to_print = shapes[tetro_type]['alt3']

        first_drawn = True
        first_drawn_x = None
        first_drawn_y = None
        for i in range(0, 5):
            for j in range(0, 5):
                if shape_to_print[i][j] == 1:

                    if first_drawn:

                        x_pos_draw = cur_x
                        y_pos_draw = cur_y
                        first_drawn_x = j
                        first_drawn_y = i

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        game.draw.rect(surface=self.surface, color=black,
                                       rect=tetro_rect)
                        first_drawn = False
                    else:
                        x_pos_draw = cur_x + ((j - first_drawn_x) * 25)
                        y_pos_draw = cur_y + ((i - first_drawn_y) * 25)

                        tetro_rect = Rect(x_pos_draw, y_pos_draw, 25, 25)
                        game.draw.rect(surface=self.surface, color=black,
                                       rect=tetro_rect)

    def current_piece_occupying(self, tetro_type, alt, shapes, cur_x, cur_y):
        shape_to_print = shapes[tetro_type]['shape']

        self.current_piece_board_spaces = []
        grid_x = int((cur_x - 175) / 25)
        grid_y = int((cur_y - 97) / 25)
        # print('grid x: ' + str(grid_x))
        # print('grid y: ' + str(grid_y))

        y_offset = 0
        first_val = True
        for i in range(0, 5):
            for j in range(0, 5):
                if shape_to_print[i][j] == 1:
                    if first_val:
                        y_offset = i
                        x_offset = j
                        self.current_piece_board_spaces.append([grid_x,
                                                                grid_y])
                        first_val = False
                    else:
                        self.current_piece_board_spaces.append(
                            [(grid_x + j - x_offset),
                             (grid_y + i - y_offset)])

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

    def update_grid_occupied(self):
        for i in range(0, 4):
            piece_val_x = self.current_piece_board_spaces[i][0]
            piece_val_y = self.current_piece_board_spaces[i][1]
            self.grid_occupied[piece_val_y][piece_val_x] = 1

    def key_press(self):
        now = game.time.get_ticks()
        key_pressed = False
        pressed_keys = game.key.get_pressed()
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
        if direction == "left":
            for i in range(0, 4):
                if self.current_piece_board_spaces[i][0] == 0:
                    return False
                piece_x_val = self.current_piece_board_spaces[i][0]
                piece_y_val = self.current_piece_board_spaces[i][1]
                if self.grid_occupied[piece_y_val][piece_x_val-1] == 1:
                    print('left occupied')
                    return False
            return True
        if direction == "right":
            for j in range(0, 4):
                if self.current_piece_board_spaces[j][0] == 9:
                    return False
                piece_x_val = self.current_piece_board_spaces[j][0]
                piece_y_val = self.current_piece_board_spaces[j][1]
                if self.grid_occupied[piece_y_val][piece_x_val+1] == 1:
                    print('right occupied')
                    return False
            return True

    def update_grid_colors(self, tetro_array, tetro_type, shapes):
        shape_color = shapes[tetro_type]['color']
        for a in tetro_array:
            self.grid_colored[a[1]][a[0]] = shape_color
        print('color was ' + str(shape_color))
        print('new colored grid: ' + str(self.grid_colored))

    def valid_rotation(self, tetro_type, alt, shapes):
        if alt == 0:
            if 'alt1' in shapes[tetro_type]:
                return 1
        elif alt == 1:
            if 'alt2' in shapes[tetro_type]:
                return 2
            else:
                return 0
        elif alt == 2:
            return 3
        else:
            return 0
            print("cannot rotate")
        return -1

    def rows_check(self):
        for i in range(0, 20):
            count = 0
            for j in range(0, 10):
                if self.grid_occupied[i][j] == 1:
                    count += 1

            if count == 10:
                self.clear_full_row(i)


    def clear_full_row(self, row):
        pass

    def update_score(self):
        pass


Tetris = Window()
