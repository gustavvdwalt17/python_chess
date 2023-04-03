from constants import *
import pygame
from square import Square
from piece import *
from piece import Piece
from move import Move


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._create_pieces()

    def handle_move(self, move, piece):
        initial = move.initial
        final = move.final
        if piece.an_passant == True and piece.color =='white' :
            self.squares[initial.row][initial.col+1].piece = None
            self.squares[initial.row][initial.col].piece = None
            self.squares[final.row][final.col].piece = piece
            piece.clear_moves()

            piece.move_count += 1
            return
        # elif piece.an_passant == True and piece.color =='white' and piece.an_passant_side == False:
        #     self.squares[initial.row][initial.col-1].piece = None
        #     self.squares[initial.row][initial.col].piece = None
        #     self.squares[final.row][final.col].piece = piece
        #     piece.clear_moves()

        #     piece.move_count += 1
        #     return
        # elif piece.an_passant == True and piece.color =='black' and piece.an_passant_side ==False:
        #     self.squares[initial.row][initial.col-1].piece = None
        #     self.squares[initial.row][initial.col].piece = None
        #     self.squares[final.row][final.col].piece = piece
        #     piece.clear_moves()

        #     piece.move_count += 1
        #     return
        # elif piece.an_passant == True and piece.color =='black' and piece.an_passant_side:
        #     self.squares[initial.row][initial.col+1].piece = None
        #     self.squares[initial.row][initial.col].piece = None
        #     self.squares[final.row][final.col].piece = piece
        #     piece.clear_moves()

        #     piece.move_count += 1
        #     return
        # piec  e = self.squares[initclickedRow][initclickedCol].piece
        # print(self.squares[0][0].piece)
        # self.squares[initclickedRow][initclickedRow].piece = Square(
        #     initclickedRow, initclickedRow)

        # for move in piece.valid_moves: check if move is in valid move
        # print('initial', initial.row)

        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        
        piece.moved = True

        # print(self.squares[initclickedRow][initclickedCol].piece)
        # self.squares[final.row][final.col].piece = pisie
        # print(self.squares[clickedRow][clickedCol], piece)
        piece.clear_moves()
        piece.move_count += 1
        if (piece.name == 'pawn'):
            self.check_valid_moves(piece,final.row,final.col)
    def check_valid(self, piece, move):
        return move in piece.valid_moves

    def check_valid_moves(self, piece, row, col):

        def knight():
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col+-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                possbile_move_row, possible_move_col = possible_move
                print(possbile_move_row, possible_move_col)
                if Square.in_range(possbile_move_row, possible_move_col):

                    if not self.squares[possbile_move_row][possible_move_col].has_piece():

                        initial = Square(row, col)
                        final = Square(possbile_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)
                    elif self.squares[possbile_move_row][possible_move_col].is_rival(piece.color):

                        initial = Square(row, col)
                        final = Square(possbile_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)
                        continue

                    # if Square.in_range(possbile_move_row, possible_move_col):
                    #     print(possbile_move_row, possible_move_col)

                else:
                    continue

        def bishop():

            counter = -1
            possible_moves = [

                (row+1, col+1),
                (row+1, col-1),
                (row-1, col-1),
                (row-1, col+1),

            ]
            possible_moves2 = [

                (1, 1),
                (1, -1),
                (-1, -1),
                (-1, +1),

            ]

            for possible_move in possible_moves:

                counter = counter + 1
                possible_move_row, possible_move_col = possible_move

                while Square.in_range(possible_move_row, possible_move_col):

                    # print(possible_moves[0][0])

                    if not Square.in_range(possible_move_col, possible_move_row):

                        break

                    # if Square.in_range(possible_move_row, possible_move_col):

                    if not self.squares[possible_move_row][possible_move_col].has_piece():

                        initial = Square(row, col)
                        final = Square(possible_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)
                        # possible_move_row_add =

                        possible_move_row = possible_move_row + \
                            possible_moves2[counter][0]
                        possible_move_col = possible_move_col + \
                            possible_moves2[counter][1]

                    elif self.squares[possible_move_row][possible_move_col].is_rival(piece.color):

                        initial = Square(row, col)
                        final = Square(possible_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)

                        possible_move_row = possible_move_row + \
                            possible_moves2[counter][0]
                        possible_move_col = possible_move_col + \
                            possible_moves2[counter][1]
                        break
                    else:
                        break

        def rook():
            counter = -1
            possible_moves = [
                (row+1, col),
                (row, col+1),
                (row, col-1),
                (row-1, col)
            ]

            possible_moves2 = [
                (1, 0),
                (0, 1),
                (0, -1),
                (-1, 0),



            ]

            for possible_move in possible_moves:

                counter = counter + 1
                possible_move_row, possible_move_col = possible_move

                while Square.in_range(possible_move_row, possible_move_col):

                    # print(possible_moves[0][0])

                    if not Square.in_range(possible_move_col, possible_move_row):

                        break

                    # if Square.in_range(possible_move_row, possible_move_col):

                    if not self.squares[possible_move_row][possible_move_col].has_piece():

                        initial = Square(row, col)
                        final = Square(possible_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)
                        # possible_move_row_add =

                        possible_move_row = possible_move_row + \
                            possible_moves2[counter][0]
                        possible_move_col = possible_move_col + \
                            possible_moves2[counter][1]

                    elif self.squares[possible_move_row][possible_move_col].is_rival(piece.color):

                        initial = Square(row, col)
                        final = Square(possible_move_row,
                                       possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)

                        possible_move_row = possible_move_row + \
                            possible_moves2[counter][0]
                        possible_move_col = possible_move_col + \
                            possible_moves2[counter][1]
                        break
                    else:
                        break

        def pawn():
            print(piece.move_count)
            if piece.moved:
                if piece.color == 'white':
                    steps = row - 1
                elif piece.color == 'black':
                    steps = row + 1
            else:
                if piece.color == 'black':
                    steps = row + 2
                    steps2 = row + 1
                else:
                    steps = row - 2
                    steps2 = row - 1
            possible_captures = [
                (row+1, col+1),
                (row-1, col-1),
                (row+1, col-1),
                (row-1, col+1),

            ]
            an_passant_moves_white = [
                (row-1, col-1),
                (row-1, col+1),

            ]
            an_passant_moves_black = [
                (row+1,col-1),
                (row+1,col+1)
            ]
#enemy piece moet nog nie beweeg het nie, as piece in row 3 kom moet daar niks links of regs wees nie
            # for rows in
            if piece.moved:
                if piece.color == 'white':
                    if row ==3 and piece.an_passant == False:
                        if self.squares[row][col+1].is_rival(piece.color):

                            thePiece = self.squares[row][col+1].piece
                            if thePiece.move_count == 1:
                                # for possible_an in an_passant_moves_white:
                                possible_an_row, possible_an_col = an_passant_moves_white[1]
                                if not self.squares[possible_an_row][possible_an_col].has_piece():
                                    # if self.squares[possible_an_row][possible_an_col].is_rival(piece.color):

                                    initial_row = Square(row, col)
                                    final = Square(possible_an_row,
                                                   possible_an_col)
                                    move = Move(initial_row, final)
                                    piece.add_moves(move)
                                    piece.moved = True
                                    piece.an_passant = True
                                    piece.an_passant_side =  True
                    #     elif self.squares[row][col-1].is_rival(piece.color):
                    #         thePiece=self.squares[row][col-1].piece
                    #         if thePiece.move_count ==1:
                    #             possible_an_row,possbile_an_col = an_passant_moves_white[0]
                    #             if not self.squares[possible_an_row][possbile_an_col].has_piece():
                    #                 initial_row = Square(row, col)
                    #                 final = Square(possible_an_row,
                    #                               possbile_an_col)
                    #                 move = Move(initial_row, final)
                    #                 piece.add_moves(move)
                    #                 piece.moved = True
                    #                 piece.an_passant = True
                    #                 piece.an_passant_side =  False

                    # if row == 3:
                    #     if self.squares[row][col+1].is_rival(piece.color):

                    #         thePiece = self.squares[row][col+1].piece
                    #         if thePiece.move_count == 1:
                    #             # for possible_an in an_passant_moves_white:
                    #             possible_an_row, possible_an_col = an_passant_moves_white[1]
                    #             if not self.squares[possible_an_row][possible_an_col].has_piece():
                    #                 # if self.squares[possible_an_row][possible_an_col].is_rival(piece.color):

                    #                 initial_row = Square(row, col)
                    #                 final = Square(possible_an_row,
                    #                                possible_an_col)
                    #                 move = Move(initial_row, final)
                    #                 piece.add_moves(move)
                    #                 piece.moved = True
                    #                 piece.an_passant = True
                    #                 piece.an_passant_side =  True
                    #     elif self.squares[row][col-1].is_rival(piece.color):
                    #         thePiece=self.squares[row][col-1].piece
                    #         if thePiece.move_count ==1:
                    #             possible_an_row,possbile_an_col = an_passant_moves_white[0]
                    #             if not self.squares[possible_an_row][possbile_an_col].has_piece():
                    #                 initial_row = Square(row, col)
                    #                 final = Square(possible_an_row,
                    #                               possbile_an_col)
                    #                 move = Move(initial_row, final)
                    #                 piece.add_moves(move)
                    #                 piece.moved = True
                    #                 piece.an_passant = True
                    #                 piece.an_passant_side =  False
        
                # if piece.color == 'black':
                #     if row == 4:
                #         if self.squares[row][col+1].in_range():
                #             if self.squares[row][col+1].is_rival(piece.color):

                #                 thePiece = self.squares[row][col+1].piece
                #                 if thePiece.move_count == 1:
                #                     # for possible_an in an_passant_moves_white:
                #                     possible_an_row, possible_an_col = an_passant_moves_black[1]
                #                     if not self.squares[possible_an_row][possible_an_col].has_piece():
                #                         # if self.squares[possible_an_row][possible_an_col].is_rival(piece.color):

                #                         initial_row = Square(row, col)
                #                         final = Square(possible_an_row,
                #                                     possible_an_col)
                #                         move = Move(initial_row, final)
                #                         piece.add_moves(move)
                #                         piece.moved = True
                #                         piece.an_passant = True
                #                         piece.an_passant_side =  True
                #             elif self.squares[row][col-1].is_rival(piece.color):
                #                 print('poweranger')
                #                 thePiece=self.squares[row][col-1].piece
                #                 if thePiece.move_count ==1:
                #                     possible_an_row,possbile_asn_col = an_passant_moves_black[0]
                #                     if not self.squares[possible_an_row][possbile_asn_col].has_piece():
                #                         initial_row = Square(row, col)
                #                         final = Square(possible_an_row,
                #                                     possbile_asn_col)
                #                         move = Move(initial_row, final)
                #                         piece.add_moves(move)
                #                         piece.moved = True
                #                         piece.an_passant = True
                #                         piece.an_passant_side =  False

                for possible_moves in possible_captures: 
                    possible_move_row, possible_move_col = possible_moves
                    if Square.in_range(possible_move_row, possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].is_rival(piece.color):
                            if (piece.color =='white' and possible_move_row < row ):

                                initial_row = Square(row, col)
                                final = Square(possible_move_row,
                                            possible_move_col)
                                move = Move(initial_row, final)
                                piece.add_moves(move)
                                piece.moved = True
                        
                            
                            elif (piece.color =='black' and possible_move_row > row  ):

                                initial_row = Square(row, col)
                                final = Square(possible_move_row,
                                            possible_move_col)
                                move = Move(initial_row, final)
                                piece.add_moves(move)
                                piece.moved = True
                        else:
                            continue
                if Square.in_range(steps, col):
                    if not self.squares[steps][col].is_rival(piece.color):
                        if not self.squares[steps][col].has_piece():

                            initial_row = Square(row, col)
                            final = Square(steps, col)
                            move = Move(initial_row, final) 
                            piece.add_moves(move)
                            piece.moved = True
            else:
                # as pawn 2 voor inital pawn is kani beweeg nie err
                # an passant
                for possible_moves in possible_captures:
                    possible_move_row, possible_move_col = possible_moves
                    if Square.in_range(possible_move_row, possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].is_rival(piece.color):
                            initial_row = Square(row, col)
                            final = Square(possible_move_row,
                                           possible_move_col)
                            move = Move(initial_row, final)
                            piece.add_moves(move)
                            piece.moved = True
                        else:
                            continue
                if Square.in_range(steps, col):
                    if not self.squares[steps][col].is_rival(piece.color):
                        if not self.squares[steps][col].has_piece():
                            initial_row = Square(row, col)
                            final = Square(steps, col)
                            move = Move(initial_row, final)
                            piece.add_moves(move)
                            piece.moved = True
                            
                            initial_row = Square(row, col)
                            final = Square(steps2, col)
                            move = Move(initial_row, final)
                            piece.add_moves(move)
                            piece.moved = True
                        
                        # an passant

        if piece.name == 'knight':
            knight()
        elif piece.name == 'pawn':
            pawn()

        elif piece.name == 'bishop':
            bishop()
        elif piece.name == 'rook':
            rook()

    def _create(self):
        for rows in range(ROWS):
            for cols in range(COLS):
                self.squares[rows][cols] = Square(rows, cols)

    def _create_pieces(self):

        for rows in range(ROWS):

            if (rows == 2 or rows == 3 or rows == 4 or rows == 5):
                continue
            if (rows == 0 or rows == 1):
                color = 'black'
            elif (rows == 6 or rows == 7):
                color = 'white'

            self.squares[rows][0] = Square(rows, 0, Rook(color))
            self.squares[rows][1] = Square(rows, 1, Bishop(color))
            self.squares[rows][2] = Square(rows, 2, Knight(color))
            self.squares[rows][3] = Square(rows, 3, Queen(color))
            self.squares[rows][4] = Square(rows, 4, King(color))
            self.squares[rows][5] = Square(rows, 5, Knight(color))
            self.squares[rows][6] = Square(rows, 6, Bishop(color))
            self.squares[rows][7] = Square(rows, 7, Rook(color))

        white = 1
        black = 6

        for pawns in range(COLS):

            self.squares[white][pawns] = Square(1, pawns, Pawn('black'))

            self.squares[black][pawns] = Square(6, pawns, Pawn('white'))

