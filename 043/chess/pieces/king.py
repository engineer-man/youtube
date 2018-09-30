from pieces import Piece
from pieces import Pawn
import board
import copy
import globVar
import utils

class King(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "K"
        else:
            return "k"

    def scan(self):
        availMoves = []
        optionCounter = 1
        pieceFound = False

        # scan up and left
        rowCount = self.row - 1
        colCount = self.col - 1
        if self.row > 0 and self.col > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan up
        pieceFound = False
        rowCount = self.row - 1
        colCount = self.col
        if self.row > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan up and right
        pieceFound = False
        rowCount = self.row - 1
        colCount = self.col + 1
        if self.row > 0 and self.col < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan right
        pieceFound = False
        rowCount = self.row
        colCount = self.col + 1
        if self.col < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

################################
        # scan down and right
        pieceFound = False
        rowCount = self.row + 1
        colCount = self.col + 1
        if self.row < 7 and self.col < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan down
        pieceFound = False
        rowCount = self.row + 1
        colCount = self.col
        if self.row < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan down and left
        pieceFound = False
        rowCount = self.row + 1
        colCount = self.col - 1
        if self.row < 7 and self.col > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan left
        pieceFound = False
        rowCount = self.row
        colCount = self.col - 1
        if self.col > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # check availMoves and remove the ones that put user in check
        # if ((self.color == "W" and globVar.w_check) or
        # (self.color == "b" and globVar.b_check) and
        # not globVar.scanning):
        #     availMoves = utils.remove_invalid_moves(availMoves, self)

        return availMoves
