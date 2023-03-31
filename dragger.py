import pygame
from constants import *


class Dragger:
    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.dragging = False
        self.piece = None
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        # tecture
        self.piece.set_texture(size=80)
        texture = self.piece.texture
        # image
        img = pygame.image.load(texture)

        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.textureRect = img.get_rect(center=img_center)

        surface.blit(img, self.piece.textureRect)

    def update_mouse_pos(self, pos):
        self.mouseX, self.mouseY = pos

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE
