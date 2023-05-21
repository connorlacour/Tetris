import pygame as pg
import numpy as np

from models.tetrominos import Tetrominos

class CurrentPiece:
    def __init__(self) -> None:
        self.tetrominos = Tetrominos()
        self.tetros = self.tetrominos.shapes
        self.tetro_types = self.tetrominos.get_types()
        self.piece = self.generate_next_piece()

    def generate_next_piece(self):
        tetro = self.tetros[np.random.choice(self.tetro_types)]
        return {
            "iterations": tetro['iterations'],
            "pos": [2, -5],
            "alt": 0,
            "color": tetro['color']
        }
    
    def get(self):
        return self.piece

    def get_shape(self):
        return self.piece['iterations'][self.piece['alt']]['shape']
    
    def increment_pos(self, coord, val):
        '''
        Updates pos attribute of piece by adding the val passed to the current pos val
        coord: 0 or 1 for x or y coordinate
        val: amount to increment (positive or negative)
        '''
        self.piece['pos'][coord] = self.piece['pos'][coord] + val