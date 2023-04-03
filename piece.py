import os


class Piece:
    def __init__(self, name, color, value, texture=None, textureRect=None):
        self.name = name
        self.color = color
        self.value = value
        self.texture = texture
        self.set_texture()
        self.textureRect = textureRect
        self.valid_moves = []
        self.moved = False
        self.move_count = 0
        self.an_passant = False
        self.an_passant_side = None
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_moves(self, move):
        self.valid_moves.append(move)

    def clear_moves(self):
        self.valid_moves = []


class Pawn(Piece):
    def __init__(self, color):
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.01)


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000)


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)
