"""
This module contains functions relating to the creation and access
of the game board.
"""

import pieces
from square import Square
import globVar
import utils

grid = []

def populate():
    place = 0
    global grid

    # fill grid with empty Squares
    for i in range(16):
        grid.append([])
        for j in range(16):
            grid[i].append(Square(False, "b", pieces.Piece("none", "pawn"), i, j))

    # alternate colors
    for i in range(8):
        if (i % 2 == 0):
            place = 0
            for j in range(8):
                grid[i][place].pieceStatus = False
                grid[i][place].color = "white"
                grid[i][place].row = i
                grid[i][place].col = place

                grid[i][place + 1].pieceStatus = False
                grid[i][place + 1].color = "black"
                grid[i][place + 1].row = i
                grid[i][place + 1].col = (place + 1)

                place += 2

        else:
            place = 0
            for k in range(8):
                grid[i][place].pieceStatus = False
                grid[i][place].color = "black"
                grid[i][place].row = i
                grid[i][place].col = place
                grid[i][place + 1].pieceStatus = False
                grid[i][place + 1].color = "white"
                grid[i][place + 1].row = i
                grid[i][place + 1].col = (place + 1)
                place += 2

    # Fill board with pieces

    # black
    plr = "b"
    Grid(0,0).piece = pieces.Rook(plr, "rook")
    Grid(0,1).piece = pieces.Knight(plr, "knight")
    Grid(0,2).piece = pieces.Bishop(plr, "bishop")
    Grid(0,3).piece = pieces.Queen(plr, "queen")
    Grid(0,4).piece = pieces.King(plr, "king")
    Grid(0,5).piece = pieces.Bishop(plr, "bishop")
    Grid(0,6).piece = pieces.Knight(plr, "knight")
    Grid(0,7).piece = pieces.Rook(plr, "rook")

    for i in range(8):
        Grid(1,i).piece = pieces.Pawn(plr, "pawn")
        Grid(1,i).piece.firstMove = True
        globVar.firstPawns.append(Grid(1,i).piece)

    # set pieceStatus and piece_ID for black pieces
    piece_ID = 0
    for i in range(2):
        for j in range(8):
            Grid(i,j).pieceStatus = True
            Grid(i,j).piece.label = piece_ID
            piece_ID += 1
            globVar.b_pieces.append(Grid(i,j).piece)

    # white
    plr = "W"
    Grid(7,0).piece = pieces.Rook(plr, "rook")
    Grid(7,1).piece = pieces.Knight(plr, "knight")
    Grid(7,2).piece = pieces.Bishop(plr, "bishop")
    Grid(7,3).piece = pieces.Queen(plr, "queen")
    Grid(7,4).piece = pieces.King(plr, "king")
    Grid(7,5).piece = pieces.Bishop(plr, "bishop")
    Grid(7,6).piece = pieces.Knight(plr, "knight")
    Grid(7,7).piece = pieces.Rook(plr, "rook")

    for i in range(8):
        Grid(6,i).piece = pieces.Pawn(plr, "pawn")
        Grid(6,i).piece.firstMove = True
        globVar.firstPawns.append(Grid(6,i).piece)

    # set pieceStatus and assign ID to white pieces
    place = 6
    piece_ID = 0
    for i in range(2):
        i = place
        for j in range(8):
            Grid(i,j).pieceStatus = True
            Grid(i,j).piece.label = piece_ID
            piece_ID += 1
            globVar.w_pieces.append(Grid(i,j).piece)
        place += 1

    # set pieceStatus to false for the rest
    place = 2
    for i in range(4):
        i = place
        for j in range(8):
            Grid(i,j).pieceStatus = False

    # copy square coordinates to pieces
    for i in range(8):
        for j in range(8):
            if Grid(i,j).pieceStatus:
                Grid(i,j).piece.row = Grid(i,j).row
                Grid(i,j).piece.col = Grid(i,j).col

    # Clip board to 8 x 8
    while len(grid) > 8:
        grid.pop()
    for i in range(8):
        while len(grid[i]) > 8:
            grid[i].pop()

    # initialize global variables
    resetGlobal()

# return reference to grid
def Grid(row, col):
    return grid[row][col]

def resetGlobal():
    globVar.player = "W"
    globVar.playerCount = 0
    globVar.w_NumPieces = 16
    globVar.b_NumPieces = 16
    globVar.r_w_NumPieces = 1
    globVar.r_b_NumPieces = 1
    globVar.w_check = False
    globVar.b_check = False
    globVar.removed = False
    globVar.removed_label = -1
    globVar.removed_color = "none"
    globVar.last_row = -1
    globVar.last_col = -1
    globVar.scanning = False
    globVar.r_avail_Num = 1
    globVar.r_w_pieces = [pieces.Pawn("none", "none")]
    globVar.r_b_pieces = [pieces.Pawn("none", "none")]
    globVar.r_avail = [Square(False, "none", pieces.Pawn("none","none"), -1, -1)]
    globVar.p_w_Moves = []
    globVar.p_b_Moves = []
    globVar.p_w_Num = -1
    globVar.p_b_Num = -1

# update grid with toSqr
def uGrid(pc):
    global grid
    # grid[toSqr.row][toSqr.col] = toSqr
    grid[pc.row][pc.col].pieceStatus = True
    grid[pc.row][pc.col].piece = pc
