import pygame as pg
import numpy as np
import config

from models.tetrominos import Tetrominos

class CurrentPiece:
    def __init__(self) -> None:
        self.tetrominos = Tetrominos()
        self.tetros = self.tetrominos.shapes
        self.tetro_types = self.tetrominos.get_types()
        self.piece = self.generate_next_piece()
        self.next_piece_pos = [13, -2]

    def generate_next_piece(self):
        tetro = self.tetros[np.random.choice(self.tetro_types)]
        return {
            "iterations": tetro['iterations'],
            "pos": [2, -5],
            "alt": 0,
            "color": tetro['color']
        }
    
    def get(self, dest=None):
        if dest in self.piece.keys():
            return self.piece[dest]    
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
    
    def is_occupied(self, coord):
        return self.get_shape()[coord[0]][coord[1]] == 1
    
    def get_next_piece_pos(self):
        return self.next_piece_pos

    def rotate(self):
        self.piece['alt'] = (self.piece['alt'] + 1) % len(self.piece['iterations'])