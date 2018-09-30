from pieces import Piece
import board

class Pawn(Piece):
    def __init__(self, color, type):
        self.firstMove = False
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "P"
        elif self.color == "b":
            return "p"
        else:
            return ""

    def scan(self):
        # Determine direction
        if self.color == "W":
            dn = -1
        else:
            dn = 1
        availMoves = []
        optionCounter = 1
        blocked = True
        doubleBlocked = True

        if ((self.row > 0 and self.color == "W") or
        (self.row < 7 and self.color == "b")):
            blocked = board.Grid((self.row + (1 * dn) ), self.col).pieceStatus

        if ((self.row > 1 and self.color == "W") or
        (self.row < 6 and self.color == "b")):
            doubleBlocked = board.Grid((self.row + (2 * dn) ), self.col).pieceStatus

        # Scan directly ahead
        if (not blocked):
            availMoves.append(board.Grid((self.row + (1 * dn) ), self.col))
            board.Grid((self.row + (1 * dn) ), self.col).des = True
            board.Grid((self.row + (1 * dn) ), self.col).option = optionCounter
            optionCounter += 1

        # Scan two spaces ahead
        if(self.firstMove and not blocked and not doubleBlocked):
            availMoves.append(board.Grid((self.row + (2 * dn) ), self.col))
            board.Grid((self.row + (2 * dn) ), self.col).des = True
            board.Grid((self.row + (2 * dn) ), self.col).option = optionCounter
            optionCounter += 1

        # Check for diagonal enemies
        # left
        if self.col > 0 and (self.row + (1 * dn)) >= 0 and (self.row + (1 * dn)) <= 7:
            diagColor = board.Grid((self.row + (1 * dn)), (self.col - 1)).piece.color

            if ( diagColor != self.color and diagColor != "none"):
                availMoves.append(board.Grid((self.row + (1 * dn)), (self.col - 1)))
                board.Grid((self.row + (1 * dn)), (self.col - 1)).des = True
                board.Grid((self.row + (1 * dn)), (self.col - 1)).option = optionCounter
                optionCounter += 1

        # right
        if self.col < 7 and (self.row + (1 * dn)) >= 0 and (self.row + (1 * dn)) <= 7:
            diagColor = board.Grid((self.row + (1 * dn)), (self.col + 1)).piece.color

            if ( diagColor != self.color and diagColor != "none"):
                availMoves.append(board.Grid((self.row + (1 * dn)), (self.col + 1)))
                board.Grid((self.row + (1 * dn)), (self.col + 1)).des = True
                board.Grid((self.row + (1 * dn)), (self.col + 1)).option = optionCounter
                optionCounter += 1

        return availMoves
