import pygame
from data.classes.Piece import Piece


class Archer(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + '_archer.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'A'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (1, -1),  # ne
            (1, 1),  # se
            (-1, 1),  # sw
            (-1, -1),  # nw
        ]
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos(
                (self.x, y)
            ))
        for square in moves_north:
            if square.occupying_piece is not None and square.occupying_piece.color is not self.color:
                moves.append((0, int(square.pos[1]) - self.y))
                break
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos(
                (x, self.y)
            ))
        for square in moves_east:
            if square.occupying_piece is not None and square.occupying_piece.color is not self.color:
                moves.append((int(square.pos[0]) - self.x, 0))
                break
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos(
                (self.x, y)
            ))
        for square in moves_south:
            if square.occupying_piece is not None and square.occupying_piece.color is not self.color:
                moves.append((0, int(square.pos[1]) - self.y))
                break
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos(
                (x, self.y)
            ))
        for square in moves_west:
            if square.occupying_piece is not None and square.occupying_piece.color is not self.color:
                moves.append((int(square.pos[0]) - self.x, 0))
                break
        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0 and new_pos[0] < 8 and new_pos[0] >= 0:
                if move[0] == 0 or move[1] == 0:
                    output.append([
                        board.get_square_from_pos(new_pos)
                    ])
                else:
                    for square in [board.get_square_from_pos(new_pos)]:
                        if square.occupying_piece is None:
                            output.append([square])
                        else:
                            break
        return output

    def attacking_squares(self, board):
        moves = self.get_moves(board)
        # return the non-diagonal moves
        return [i for i in moves if i.x == self.x or i.y == self.y]