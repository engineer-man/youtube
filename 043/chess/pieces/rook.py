from pieces import Piece
import board

class Rook(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "R"
        else:
            return "r"

    def scan(self):
        availMoves = []
        optionCounter = 1
        pieceFound = False
        running = True

        rowCount = self.row
        colCount = self.col

        # scan above
        while rowCount - 1 > -1 and running:
            rowCount -= 1
            if (board.Grid(rowCount, self.col).piece.color != self.color):
                board.Grid(rowCount, self.col).des = True
                board.Grid(rowCount, self.col).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, self.col))
                if board.Grid(rowCount, self.col).pieceStatus:
                    pieceFound = True

            else:
                rowCount = 0
                running = False

            if pieceFound:
                rowCount = 0
                running = False

        # scan below
        rowCount = self.row
        running = True
        pieceFound = False
        while rowCount + 1 < 8 and running:
            rowCount += 1
            if (board.Grid(rowCount, self.col).piece.color != self.color):
                board.Grid(rowCount, self.col).des = True
                board.Grid(rowCount, self.col).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(rowCount, self.col))
                if board.Grid(rowCount, self.col).pieceStatus:
                    pieceFound = True
            else:
                rowCount = 7
                running = False
            if pieceFound:
                rowCount = 7
                running = False

        # scan right
        running = True
        pieceFound = False
        while colCount + 1 < 8 and running:
            colCount += 1

            if (board.Grid(self.row, colCount).piece.color != self.color):
                board.Grid(self.row, colCount).des = True
                board.Grid(self.row, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(self.row, colCount))
                if board.Grid(self.row, colCount).pieceStatus:
                    pieceFound = True
            else:
                colCount = 7
                running = False
            if pieceFound:
                colCount = 7
                running = False

        # scan left
        colCount = self.col
        running = True
        pieceFound = False
        while colCount - 1 > -1 and running:
            colCount -= 1

            if (board.Grid(self.row, colCount).piece.color != self.color):
                board.Grid(self.row, colCount).des = True
                board.Grid(self.row, colCount).option = optionCounter
                optionCounter += 1
                availMoves.append(board.Grid(self.row, colCount))
                if board.Grid(self.row, colCount).pieceStatus:
                    pieceFound = True
            else:
                colCount = 0
                running = False
            if pieceFound:
                colCount = 0
                running = False


        return availMoves
