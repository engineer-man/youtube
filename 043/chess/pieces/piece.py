class Piece:
    def __init__(self, color, type):
        self.color = color
        self.selected = False
        self.type = type
        self.label = -1
        self.row = -1
        self.col = -1

    def scan(self):
        availMoves = []
        return availMoves

    # def __str__(self):
    #     if self.des:
    #         return "*" + self.label
    #
    #     elif self.selected:
    #         return "[]"
    #
    #     elif self.color == "white" and self.type == "pawn":
    #         return " p"
    #
    #     else:
    #         return "TM"
