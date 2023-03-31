import pygame
import sys
from constants import *
from board import Board
from square import Square
from game import Game
from dragger import Dragger
from move import Move


class Main:
    def __init__(self):
        pygame.init()
        # self.board = Board()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption('lChess')
        # self.square = Square()
        self.game = Game()
        # self.dragger = Dragger()

    def mainloop(self):
        # screen = self.board
        board = self.game.board
        dragger = self.game.dragger
        game = self.game

        # square = self.square
        while True:

            game.print_board(self.screen)
            game.show_moves(self.screen)
            game.show_pieces(self.screen)

            if dragger.dragging:

                dragger.update_blit(self.screen)
            # square._create
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    dragger.update_mouse_pos(event.pos)
                    initclickedRow = dragger.mouseY // SQSIZE
                    initclickedCol = dragger.mouseX//SQSIZE
                    print(initclickedRow, initclickedCol)
                    if board.squares[initclickedRow][initclickedCol].has_piece():
                        piece = board.squares[initclickedRow][initclickedCol].piece
                        if (game.turn == piece.color):
                            print(piece.move_count)
                            # dragger.save_initial(event.pos)

                            board.check_valid_moves(
                                piece, initclickedRow, initclickedCol)
                            dragger.drag_piece(piece)
                            game.print_board(self.screen)
                            game.show_moves(self.screen)
                            game.show_pieces(self.screen)
                        else:
                            break
                    else:
                        break

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:

                        dragger.update_mouse_pos(event.pos)

                        game.print_board(self.screen)
                        game.show_moves(self.screen)
                        game.show_pieces(self.screen)
                        dragger.update_blit(self.screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse_pos(event.pos)
                        clickedRow = dragger.mouseY // SQSIZE
                        clickedCol = dragger.mouseX//SQSIZE
                        piece = dragger.piece
                        print(piece)
                        initial = Square(initclickedRow,
                                         initclickedCol)
                        final = Square(clickedRow, clickedCol)
                        move = Move(initial, final)

# check where click release if that cord is in valid moves
                        if board.check_valid(piece, move):

                            board.handle_move(move, piece)
                            game.print_board(self.screen)
                            # game.show_moves(self.screen)
                            game.show_pieces(self.screen)
                            game.handle_turn()
                           # print('yes')
                        # if (clickedRow, clickedCol) in (move.final.possbile_move_row, move.final.possible_move_col):

                        # board.handle_move(
                        #     move.initial, move.final, dragger.piece)

                        # game.print_board(self.screen)
                        # game.show_moves(self.screen)
                        # game.show_pieces(self.screen)

                    dragger.undrag_piece()

                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()


main = Main()
main.mainloop()
