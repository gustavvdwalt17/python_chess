import pygame
from constants import *
from board import Board
from dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.turn = 'white'

    def print_board(self, surface):

        for rows in range(8):
            for cols in range(8):
                if (cols+rows) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                # x-axis,y-axis,width,height
                rect = (cols * SQSIZE, rows*SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_moves(self, surface):

        if self.dragger.dragging:

            piece = self.dragger.piece

            for move in piece.valid_moves:

                # print(piece.valid_moves)
                # color
                color = '#C86464' if (
                    move.final.row+move.final.col) % 2 == 0 else '#C84646'
                # rect

                rect = (move.final.col*SQSIZE, move.final.row *
                        SQSIZE, SQSIZE, SQSIZE)  # x,y,width,height

                # blit

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):

        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():

                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        # if piece is not self.dragger.piece
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col*SQSIZE+50, row*SQSIZE+50
                        piece.textureRect = img.get_rect(center=img_center)
                        # https://stackoverflow.com/questions/42577197/pygame-how-to-correctly-use-get-rectFirst, images/pygame.Surfaces don't have a position, so you have to store the blit position in the rect. When you call the get_rect method of a pygame.Surface, Pygame creates a new rect with the size of the image and the x, y coordinates (0, 0). To give the rect other coords during the instantiation you can pass an argument to get_rect, mostly center or topleft is used. To move the rect later, you can change any of these attributes of the rect:
                        # screen.blit(background,(x,y))
                        surface.blit(img,  piece.textureRect)

    def handle_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        elif self.turn == 'black':
            self.turn = 'white'
