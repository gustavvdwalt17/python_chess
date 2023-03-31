class Square:
    def __init__(self, row, col, piece=None):

        self.row = row
        self.col = col
        self.piece = piece

    def __eq__(self, other):

        return self.row == other.row and self.col == other.col

    def has_piece(self):

        return self.piece is not None

    def is_rival(self, color):

        if self.piece is None:
            return False

        # print('self color', self.piece.color, color)
        if self.piece.color != color:

            return True
        else:
            return False

    @staticmethod
    def in_range(*args):

        for arg in args:
            print('arg', arg)
            if arg < 0 or arg > 7:
                return False

        return True
