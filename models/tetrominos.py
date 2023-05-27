import pygame as pg
import copy
from utils.color_dict import ColorDict

colors = ColorDict().colors

class Tetrominos:
    def __init__(self) -> None:
        self.shapes = {
            'I': {
                'iterations': {
                    0: { "points": [[2, 0], [2, 1], [2, 2], [2, 3]] },
                    1: { "points": [[0, 2], [1, 2], [2, 2], [3, 2]] }
                },
                'color': colors['water_blue'],
                'color_name': 'water_blue'

            },
            'J': {
                'iterations': {
                    0: { "points": [[1, 1], [1, 2], [2, 2], [3, 2]] },
                    1: { "points": [[2, 1], [2, 2], [2, 3], [3, 1]] },
                    2: { "points": [[1, 2], [2, 2], [3, 2], [3, 3]] },
                    3: { "points": [[2, 1], [2, 2], [2, 3], [1, 3]] }
                },
                'color': colors['dark_blue'],
                'color_name': 'dark_blue'
            },
            'L': {
                'iterations': {
                    0: { "points": [[3, 1], [1, 2], [2, 2], [3, 2]] },
                    1: { "points": [[2, 1], [2, 2], [2, 3], [3, 3]] },
                    2: { "points": [[1, 2], [2, 2], [3, 2], [1, 3]] },
                    3: { "points": [[1, 1], [2, 1], [2, 2], [2, 3]] }
                },
                'color': colors['orange'],
                'color_name': 'orange'
            },
            'Z': {
                'iterations': {
                    0: { "points": [[1, 2], [2, 2], [2, 3], [3, 3]] },
                    1: { "points": [[2, 1], [1, 2], [2, 2], [1, 3]] }
                },
                'color': colors['bright_red'],
                'color_name': 'bright_red'
            },
            'S': {
                'iterations': {
                    0: { "points": [[2, 2], [3, 2], [1, 3], [2, 3]] },
                    1: { "points": [[2, 1], [2, 2], [3, 2], [3, 3]] }
                },
                'color': colors['green'],
                'color_name': 'green'
            },
            'T': {
                'iterations': {
                    0: { "points": [[2, 1], [1, 2], [2, 2], [3, 2]] },
                    1: { "points": [[2, 1], [2, 2], [2, 3], [3, 2]] },
                    2: { "points": [[1, 2], [2, 2], [3, 2], [2, 3]] },
                    3: { "points": [[2, 1], [1, 2], [2, 2], [2, 3]] }
                },
                'color': colors['purple'],
                'color_name': 'purple'
            },
            'O': {
                'iterations': {
                    0: { "points": [[1, 2], [2, 2], [1, 3], [2, 3]] }
                },
                'color': colors['bright_yellow'],
                'color_name': 'bright_yellow'
            }
        }

        self.generate_tetro_shapes()

    def generate_tetro_shapes(self):
        w, h = 5, 5

        blank_shape = [[0 for y in range(h)] for x in range(w)]
        for i in self.shapes.keys():
            for k, v in self.shapes[i]['iterations'].items():
                self.shapes[i]['iterations'][k]['shape'] = copy.deepcopy(blank_shape)
                for coord in v['points']:
                    self.shapes[i]['iterations'][k]['shape'][coord[1]][coord[0]] = 1
    
    def get_types(self):
        return list(self.shapes.keys())