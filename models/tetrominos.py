import pygame as pg
import copy

class Tetrominos:
    def __init__(self) -> None:
        self.shapes = {
            'I': {
                'iterations': {
                    0: { "points": [[0, 2], [1, 2], [2, 2], [3, 2]] },
                    1: { "points": [[2, 0], [2, 1], [2, 2], [2, 3]] }
                },
                'color': (25, 255, 255)
            },
            'J': {
                'iterations': {
                    0: { "points": [[1, 1], [2, 1], [2, 2], [2, 3]] },
                    1: { "points": [[1, 2], [1, 3], [2, 2], [3, 2]] },
                    2: { "points": [[2, 1], [2, 2], [2, 3], [3, 3]] },
                    3: { "points": [[1, 2], [2, 2], [3, 1], [3, 2]] }
                },
                'color': (64, 25, 255)
            },
            'L': {
                'iterations': {
                    0: { "points": [[1, 3], [2, 1], [2, 2], [2, 3]] },
                    1: { "points": [[1, 2], [2, 2], [3, 2], [3, 3]] },
                    2: { "points": [[2, 1], [2, 2], [2, 3], [3, 1]] },
                    3: { "points": [[1, 1], [1, 2], [2, 2], [3, 2]] }
                },
                'color': (255, 153, 51)
            },
            'Z': {
                'iterations': {
                    0: { "points": [[2, 1], [2, 2], [3, 2], [3, 3]] },
                    1: { "points": [[1, 2], [2, 1], [2, 2], [3, 1]] }
                },
                'color': (255, 51, 51)
            },
            'S': {
                'iterations': {
                    0: { "points": [[2, 2], [2, 3], [3, 1], [3, 2]] },
                    1: { "points": [[1, 2], [2, 2], [2, 3], [3, 3]] }
                },
                'color': (25, 255, 140)
            },
            'T': {
                'iterations': {
                    0: { "points": [[1, 2], [2, 1], [2, 2], [2, 3]] },
                    1: { "points": [[1, 2], [2, 2], [2, 3], [3, 2]] },
                    2: { "points": [[2, 1], [2, 2], [2, 3], [3, 2]] },
                    3: { "points": [[1, 2], [2, 2], [2, 1], [3, 2]] }
                },
                'color': (136, 0, 204)
            },
            'O': {
                'iterations': {
                    0: { "points": [[2, 1], [2, 2], [3, 1], [3, 2]] }
                },
                'color': (255, 255, 51)
            }
        }

        self.generate_tetro_shapes()


    def generate_tetro_shapes(self):
        w, h = 5, 5

        blank_shape = [[0 for x in range(w)] for y in range(h)]
        for i in self.shapes.keys():
            for k, v in self.shapes[i]['iterations'].items():
                self.shapes[i]['iterations'][k]['shape'] = copy.deepcopy(blank_shape)
                for coord in v['points']:
                    self.shapes[i]['iterations'][k]['shape'][coord[0]][coord[1]] = 1
        