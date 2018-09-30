from pieces import Piece
import board

class Knight(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "N"
        else:
            return "n"

    def scan(self):
        availMoves = []
        optionCounter = 1
        pieceFound = False

        # scan 2 up 1 left
        rowCount = self.row - 2
        colCount = self.col - 1
        if self.row > 1 and self.col > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 2 up 1 right
        rowCount = self.row - 2
        colCount = self.col + 1
        if self.row > 1 and self.col < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 1 up 2 right
        rowCount = self.row - 1
        colCount = self.col + 2
        if self.row > 0 and self.col < 6:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 1 down 2 right
        rowCount = self.row + 1
        colCount = self.col + 2
        if self.row < 7 and self.col < 6:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 2 down 1 right
        rowCount = self.row + 2
        colCount = self.col + 1
        if self.row < 6 and self.col < 7:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 2 down 1 left
        rowCount = self.row + 2
        colCount = self.col - 1
        if self.row < 6 and self.col > 0:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 1 down 2 left
        rowCount = self.row + 1
        colCount = self.col - 2
        if self.row < 7 and self.col > 1:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        # scan 1 up 2 left
        rowCount = self.row - 1
        colCount = self.col - 2
        if self.row > 0 and self.col > 1:
            if (board.Grid(rowCount, colCount).piece.color != self.color):
                board.Grid(rowCount, colCount).des = True
                board.Grid(rowCount, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, colCount))
                if board.Grid(rowCount, colCount).pieceStatus:
                    pieceFound = True

        return availMoves
