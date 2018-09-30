from pieces import Piece
import board

class Queen(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "Q"
        else:
            return "q"

    def scan(self):
        # rook code
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


#####################################
        # bishop code
        pieceFound = False
        running = True
        edgeFound = False

        # reset rowCount and colCount
        rowCount = self.row
        colCount = self.col

        # scan up
        if self.row > 0:
            if self.col > 0:
                # scan up and left
                while (rowCount - 1 > -1 or colCount - 1 > -1) and running and not edgeFound:
                    rowCount -= 1
                    colCount -= 1
                    if colCount == -1 or rowCount == -1:
                        edgeFound = True

                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 0
                        colCount = 0
                        running = False

                    if pieceFound:
                        rowCount = 0
                        colCount = 0
                        running = False

            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            if self.col < 7:
                # scan up and right
                while (rowCount - 1 > -1 or colCount + 1 < 8) and running and not edgeFound:
                    rowCount -= 1
                    colCount += 1
                    if colCount == 7 or rowCount == 0:
                        edgeFound = True
                    if (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 0
                        colCount = 7
                        running = False

                    if pieceFound:
                        rowCount = 0
                        colCount = 7
                        running = False

        #scan down
        if self.row < 7:
            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            # scan down and left
            if self.col > 0:
                while (rowCount + 1 < 8 or colCount - 1 > -1) and running and not edgeFound:
                    rowCount += 1
                    colCount -= 1
                    if colCount == -1 or rowCount == 8:
                        edgeFound = True
                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 7
                        colCount = 0
                        running = False

                    if pieceFound:
                        rowCount = 7
                        colCount = 0
                        running = False

            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            # scan down and right
            if self.col < 7:
                while (rowCount + 1 < 8 or colCount + 1 < 8) and running and not edgeFound:
                    rowCount += 1
                    colCount += 1
                    if colCount == 8 or rowCount == 8:
                        edgeFound = True
                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 7
                        colCount = 7
                        running = False

                    if pieceFound:
                        rowCount = 7
                        colCount = 7
                        running = False

        return availMoves
