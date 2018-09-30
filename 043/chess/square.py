import pieces
import platform

# a_block = str(chr(219) + chr(219))
u_block = u'\u2588\u2588'
a_block = u'\u2588\u2588'

class Square:
    """
    The Square class contains a piece and data such as color,
    position, and several boolean values.
    """
    def __init__(self, pieceStatus, color, piece, row, col):
        self.pieceStatus = pieceStatus
        self.color = color
        self.piece = piece
        self.row = row
        self.col = col
        self.des = False
        self.option = 0

    def __str__(self):

        global a_block
        global u_block

        if self.des:
            if self.pieceStatus and self.option < 10:
                print(self.piece, end = "")
            elif self.option < 10:
                print(" ",end="")

            print(self.option, end="")

        elif self.pieceStatus:

            print(self.piece, end="")
            if self.piece.selected:
                print("^",end="")
            else:
                if self.piece.color == "W":
                    print("'", end="")
                elif self.piece.color == "b":
                    print(".", end="")

        else:
            if self.color == "black":
                if platform.system() == "Windows":
                    return a_block
                else:
                    return u_block
            elif self.color == "white":
                return "  "

        return ""
