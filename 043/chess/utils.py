"""
This module contains miscellaneous functions necessary to the function
of this program.
"""

import Canvas
import board
import globVar
import copy
from square import Square
from pieces import Piece
import pieces
import random
import os

def check_pawn(pc):
    if (pc.type == "pawn" and (globVar.player == "W" and
    pc.row == 0) or (globVar.player == "b" and pc.row == 7)):
        if ((globVar.numPlayers == 1 and globVar.player == "W")
        or globVar.numPlayers == 2):
            choice = Canvas.pawn_to_new()
        else:
            choice = random.randint(1, 4)

        color = pc.color
        label = pc.label
        row = pc.row
        col = pc.col

        if choice == 1:
            pc = pieces.Rook(color, "rook")
        elif choice == 2:
            pc = pieces.Knight(color, "knight")
        elif choice == 3:
            pc = pieces.Bishop(color, "bishop")
        elif choice == 4:
            pc = pieces.Queen(color, "queen")

        pc.label = label
        pc.row = row
        pc.col = col

        updatePieces(pc)
        board.uGrid(pc)

def clearAllOptions():
    for i in range(8):
        for j in range(8):
            board.Grid(i,j).option = 0
            board.Grid(i,j).des = False

def potenial_moves():
    # reset p_w_moves and p_b_moves
    globVar.p_w_moves = []
    globVar.p_b_moves = []
    globVar.p_w_Num = 0
    globVar.p_b_Num = 0

    # populate p_w_Moves
    for i in range(len(globVar.w_pieces)):
        fpc = globVar.w_pieces[i]
        am = fpc.scan()
        globVar.r_avail = copy.deepcopy(am)
        globVar.r_avail_Num = len(am)
        am = mark_invalid_moves(am, fpc)
        globVar.p_w_moves.extend(am)
        # globVar.p_w_Num += len(am)
        board.Grid(globVar.w_pieces[i].row, globVar.w_pieces[i].col).piece.selected = False
    # un_resetAvailMoves(globVar.p_w_moves)
    resetAvailMoves(globVar.p_w_moves)
    globVar.p_w_Num = len(globVar.p_w_moves)

    # populate p_b_Moves
    for i in range(len(globVar.b_pieces)):
        fpc = globVar.b_pieces[i]
        am = fpc.scan()
        globVar.r_avail = copy.deepcopy(am)
        globVar.r_avail_Num = len(am)
        am = mark_invalid_moves(am, fpc)
        am = remove_invalid_moves(am)
        globVar.p_b_moves.extend(am)
        # globVar.p_b_Num += len(am)
        board.Grid(globVar.b_pieces[i].row, globVar.b_pieces[i].col).piece.selected = False
    # un_resetAvailMoves(globVar.p_b_moves)
    resetAvailMoves(globVar.p_b_moves)
    globVar.p_b_Num = len(globVar.p_b_moves)
    clearAllOptions()

def remove_invalid_moves(availMoves):
    i = 0
    while i < len(availMoves):
        if globVar.r_avail[i].option == -2:
            # board.Grid(availMoves[i].row, availMoves[i].col).des = False
            # board.Grid(availMoves[i].row, availMoves[i].col).option = -2
            availMoves.pop(i)
            globVar.r_avail.pop(i)
            globVar.r_avail_Num = len(globVar.r_avail)
            i -= 1
        i += 1

    return availMoves

def mark_invalid_moves(availMoves, pc):
    fpc = copy.deepcopy(pc)
    am = copy.deepcopy(availMoves)
    for i in range(len(availMoves)):
        move(board.Grid(fpc.row, fpc.col), am, i + 1)
        check_king()

        # undo move
        undoMove()
        pc.color = fpc.color
        # un_resetAvailMoves(am)

        # if still in check, pop move from availMoves
        if ((pc.color == "W" and globVar.w_check) or
        (pc.color == "b" and globVar.b_check)):
            board.Grid(availMoves[i].row, availMoves[i].col).des = False
            board.Grid(availMoves[i].row, availMoves[i].col).option = -2
            availMoves[i].option = -2
            globVar.r_avail[i].option = -2
        # print(pc.color, globVar.b_check, availMoves[i].option)
        # input("")

    availMoves = remove_invalid_moves(availMoves)
    return availMoves

def checkWin():
    won = False
    potenial_moves()

    if (globVar.p_w_Num == 0 or len(globVar.p_w_moves) == 0 or
    len(globVar.w_pieces) == 1 or globVar.no_w_king):
        # Canvas.clear()
        won = True
        globVar.checkmate = True
        Canvas.drawBoard()
        print(" Black wins!")
        print("\n Press Enter to exit.")
        input("")
        delete_save()

    elif (globVar.p_b_Num == 0 or len(globVar.p_b_moves) == 0 or
    len(globVar.b_pieces) == 1 or globVar.no_b_king):
        # Canvas.clear()
        won = True
        globVar.checkmate = True
        Canvas.drawBoard()
        print(" White wins!")
        print("\n Press Enter to exit.")
        input("")
        delete_save()

    return won

def check_king():
    found_b_check = False
    found_w_check = False
    # scanning flag is needed to prevent recursion
    globVar.scanning = True
    # check white pieces again black king
    for i in range(len(globVar.w_pieces)):
        fpc = globVar.w_pieces[i]
        am = fpc.scan()

        # check availMoves for every white piece
        for j in range(len(am)):
            if (am[j].piece.type == "king" and fpc.color == "W" and
            am[j].piece.color == "b"):
                globVar.b_check = True
                found_b_check = True
        resetAvailMoves(am)

    for i in range(len(globVar.b_pieces)):
        fpc = globVar.b_pieces[i]
        am = fpc.scan()

        for j in range(len(am)):
            if (am[j].piece.type == "king" and fpc.color == "b" and
            am[j].piece.color == "W"):
                globVar.w_check = True
                found_w_check = True
        resetAvailMoves(am)

    if not found_w_check:
        globVar.w_check = False
    if not found_b_check:
        globVar.b_check = False
    globVar.scanning = False
    clearAllOptions()

def resetAvailMoves(availMoves):
    for i in range(len(availMoves)):
        if availMoves[i].option != -2:
            optionRow = availMoves[i].row
            optionCol = availMoves[i].col
            board.Grid(optionRow,optionCol).des = False
            board.Grid(optionRow,optionCol).piece.selected = False
            board.Grid(optionRow,optionCol).option = 0

def un_resetAvailMoves(availMoves):
    for i in range(len(availMoves)):
        # if availMoves[i].option > -1:
        optionRow = availMoves[i].row
        optionCol = availMoves[i].col
        board.Grid(optionRow,optionCol).des = True
        # board.Grid(optionRow,optionCol).piece.selected = True
        board.Grid(optionRow,optionCol).option = i + 1

def move(fromSqr, availMoves, choice):
    pc = copy.deepcopy(fromSqr.piece)
    pc.color = fromSqr.piece.color
    pc.type = fromSqr.piece.type
    track_last_pos(pc)

    toSqr = copy.deepcopy(availMoves[choice - 1])
    deletePiece(toSqr.piece, fromSqr.piece)
    recordMove(fromSqr, toSqr)

    pc.row = toSqr.row
    pc.col = toSqr.col
    pc.selected = False

    #reset availMoves
    resetAvailMoves(availMoves)
    # update board with new piece
    board.uGrid(pc)
    updatePieces(pc)

    #turn off piece for fromSqr
    board.Grid(fromSqr.row,fromSqr.col).pieceStatus = False
    board.Grid(fromSqr.row,fromSqr.col).piece.color = "none"

    if pc.type == "pawn":
        pc.firstMove = False

    return pc

def updatePieces(pc):
    index = findIndex(pc.label, pc.color)
    if pc.color == "W":
        globVar.w_pieces[index] = pc
    elif pc.color == "b":
        globVar.b_pieces[index] = pc

def findIndex(label, c):
    i = 0
    if c == "W":
        while True:
            if globVar.w_pieces[i].label == label:
                return i
            else:
                i += 1
    elif c == "b":
        while True:
            if globVar.b_pieces[i].label == label:
                return i
            else:
                i += 1

def find_r_Index(label, c):
    i = 0
    if c == "W":
        while True:
            if globVar.r_w_pieces[i].label == label:
                return i
            else:
                i += 1
    else:
        while True:
            if globVar.r_b_pieces[i].label == label:
                return i
            else:
                i += 1

def findKingIndex(c):
    i = 0
    if c == "W":
        while True:
            if globVar.w_pieces[i].type == "king":
                return i
            else:
                i += 1
    else:
        while True:
            if globVar.b_pieces[i].type == "king":
                return i
            else:
                i += 1

def deletePiece(tpc, fpc):
    if (fpc.color != tpc.color and tpc.color != "none"):
        globVar.removed = True
        globVar.removed_label = tpc.label
        globVar.removed_color = tpc.color
        index = findIndex(tpc.label, tpc.color)
        if fpc.color == "W":
            globVar.r_b_pieces.append(tpc)
            globVar.b_pieces.pop(index)
            globVar.b_NumPieces -= 1
            globVar.r_b_NumPieces += 1
            if tpc.type == "king":
                globVar.no_b_king = True
        else:
            globVar.r_w_pieces.append(tpc)
            globVar.w_pieces.pop(index)
            globVar.w_NumPieces -= 1
            globVar.r_w_NumPieces += 1
            if tpc.type == "king":
                globVar.no_w_king = True

    # scan board and remove any pieces with same label and color
    remove_from_board(tpc.label, tpc.color)

def un_deletePiece(fpc):
    if globVar.removed:
        index = find_r_Index(globVar.removed_label, globVar.removed_color)
        if fpc.color == "W":
            tmp_pc = copy.deepcopy(globVar.r_b_pieces[index])
            globVar.b_pieces.append(tmp_pc)
            globVar.r_b_pieces.pop(index)
            globVar.b_NumPieces += 1
            globVar.r_b_NumPieces -= 1
            if tmp_pc.type == "king":
                globVar.no_b_king = False
        else:
            tmp_pc = copy.deepcopy(globVar.r_w_pieces[index])
            globVar.w_pieces.append(tmp_pc)
            globVar.r_w_pieces.pop(index)
            globVar.w_NumPieces += 1
            globVar.r_w_NumPieces -= 1
            if tmp_pc.type == "king":
                globVar.no_w_king = False

        # put piece back on board
        board.uGrid(tmp_pc)

def remove_from_board(label, color):
    for i in range(8):
        for j in range(8):
            if (board.Grid(i,j).piece.label == label and
            board.Grid(i,j).piece.color == color):
                board.Grid(i,j).piece.type = "none"
                board.Grid(i,j).piece.color = "none"
                board.Grid(i,j).pieceStatus = False

def track_last_pos(pc):
    globVar.last_row = pc.row
    globVar.last_col = pc.col

def r_c(x):
    if x == 'c': # col
        choice = Canvas.chooseCol()
        choice = choice.upper()
        choice = ord(choice)
        choice -= 65

    else: # row
        choice = Canvas.chooseRow()
        choice = (8 - choice)

    return int(choice)

def writeSave():
    startData = "True"
    save = open("chess.save","w")

    save.write(startData)
    save.write("\n")

    # write board
    writeBoard(save)
    # write global variables
    writeGlobal(save)
    # write pieces arrays
    writePiecesArrays(save)
    # write deleted pieces arrays
    write_r_PiecesArrays(save)
    # write potenial moves
    write_p_moves(save)
    # write firstPawns
    write_firstPawns(save)

    save.write("\n")
    save.close()

def readSave():
    save = open("chess.save", "r")
    startData = save.readline().strip('\n')
    if startData == "True":
        st = True
    else:
        st = False

    if st:
        # read board
        readBoard(save)
        # read global variables
        readGlobal(save)
        # read w_pieces and b_pieces
        readPiecesArrays(save, "W")
        readPiecesArrays(save, "b")
        # read deleted pieces
        read_r_PiecesArrays(save, "W")
        read_r_PiecesArrays(save, "b")
        # read r_avail
        read_r_avail(save)
        # read p_moves
        read_p_moves(save)
        # read firstPawns
        read_firstPawns(save)

def readBoard(save):
    board.populate()
    k = 0
    sqrArray = save.readline().split(',')

    for i in range(8):
        for j in range(8):

            ps = sqrArray[k]
            if ps == "True":
                pieceStatus = True
            else:
                pieceStatus = False
            k += 1
            board.Grid(i,j).color = sqrArray[k]
            k += 1
            board.Grid(i,j).row = int(sqrArray[k])
            k += 1
            board.Grid(i,j).col = int(sqrArray[k])
            k += 1
            board.Grid(i,j).des = False
            k += 1
            board.Grid(i,j).option = int(sqrArray[k])
            k += 1

            type = sqrArray[k]
            k += 1
            color = sqrArray[k]
            k += 1
            selected = False
            k += 1
            label = int(sqrArray[k])
            k += 1
            row = int(sqrArray[k])
            k += 1
            col = int(sqrArray[k])
            k += 1

            pc = pieceConstructor(color, type)
            board.Grid(i,j).piece = pc
            board.Grid(i,j).piece.selected = selected
            board.Grid(i,j).piece.label = label
            board.Grid(i,j).piece.row = row
            board.Grid(i,j).piece.col = col
            board.Grid(i,j).pieceStatus = pieceStatus

def readGlobal(save):
    globVar.numPlayers = int(save.readline().strip('\n'))
    globVar.player = save.readline().strip('\n')
    noPlayers = save.readline().strip('\n')
    if noPlayers == "True":
        globVar.noplayers = True
    else:
        globVar.noPlayers = False
    globVar.playerCount = int(save.readline().strip('\n'))
    globVar.w_NumPieces = int(save.readline().strip('\n'))
    globVar.b_NumPieces = int(save.readline().strip('\n'))
    globVar.r_w_NumPieces = int(save.readline().strip('\n'))
    globVar.r_b_NumPieces = int(save.readline().strip('\n'))
    w_check = save.readline().strip('\n')
    b_check = save.readline().strip('\n')
    removed = save.readline().strip('\n')
    if w_check == "True":
        globVar.w_check = True
    else:
        globVar.w_check = False
    if b_check == "True":
        globVar.b_check = True
    else:
        globVar.w_check = False
    if removed == "True":
        globVar.removed = True
    else:
        globVar.removed = False
    globVar.removed_label = int(save.readline().strip('\n'))
    globVar.removed_color = save.readline().strip('\n')
    globVar.last_col = int(save.readline().strip('\n'))
    globVar.last_row = int(save.readline().strip('\n'))
    scanning = save.readline().strip('\n')
    if scanning == "True":
        globVar.scanning = True
    else:
        globVar.scanning = False
    globVar.r_avail_Num = int(save.readline().strip('\n'))
    globVar.p_w_Num = int(save.readline().strip('\n'))
    globVar.p_b_Num = int(save.readline().strip('\n'))
    m_f_ps = save.readline().strip('\n')
    if m_f_ps == "True":
        globVar.m_f_ps = True
    else:
        globVar.m_f_ps = False
    globVar.m_f_p_color = save.readline().strip('\n')
    globVar.m_f_p_type = save.readline().strip('\n')
    globVar.m_f_p_label = int(save.readline().strip('\n'))
    globVar.m_f_p_row = int(save.readline().strip('\n'))
    globVar.m_f_p_col = int(save.readline().strip('\n'))
    m_t_ps = save.readline().strip('\n')
    if m_t_ps == "True":
        globVar.m_t_ps = True
    else:
        globVar.m_t_ps = False
    globVar.m_t_p_color = save.readline().strip('\n')
    globVar.m_t_p_type = save.readline().strip('\n')
    globVar.m_t_p_label = int(save.readline().strip('\n'))
    globVar.m_t_p_row = int(save.readline().strip('\n'))
    globVar.m_t_p_col = int(save.readline().strip('\n'))
    m_fm = save.readline().strip('\n')
    if m_fm == "True":
        globVar.m_fm = True
    else:
        globVar.m_fm = False

    u_m_f_ps = save.readline().strip('\n')
    if u_m_f_ps == "True":
        globVar.u_m_f_ps = True
    else:
        globVar.u_m_f_ps = False
    globVar.u_m_f_p_color = save.readline().strip('\n')
    globVar.u_m_f_p_type = save.readline().strip('\n')
    globVar.u_m_f_p_label = int(save.readline().strip('\n'))
    globVar.u_m_f_p_row = int(save.readline().strip('\n'))
    globVar.u_m_f_p_col = int(save.readline().strip('\n'))
    u_m_t_ps = save.readline().strip('\n')
    if u_m_t_ps == "True":
        globVar.u_m_t_ps = True
    else:
        globVar.u_m_t_ps = False
    globVar.u_m_t_p_color = save.readline().strip('\n')
    globVar.u_m_t_p_type = save.readline().strip('\n')
    globVar.u_m_t_p_label = int(save.readline().strip('\n'))
    globVar.u_m_t_p_row = int(save.readline().strip('\n'))
    globVar.u_m_t_p_col = int(save.readline().strip('\n'))
    u_m_fm = save.readline().strip('\n')
    if u_m_fm == "True":
        globVar.u_m_fm = True
    else:
        globVar.u_m_fm = False
    no_b_king = save.readline().strip('\n')
    if no_b_king == "True":
        globVar.no_b_king = True
    else:
        globVar.no_b_king = False
    no_w_king = save.readline().strip('\n')
    if no_w_king == "True":
        globVar.no_w_king = True
    else:
        globVar.no_w_king = False
    globVar.firstPawnsNum = int(save.readline().strip('\n'))
    checkmate = save.readline().strip('\n')
    if checkmate == "True":
        globVar.checkmate = True
    else:
        globVar.checkmate = False
    slow_speed = save.readline().strip('\n')
    if slow_speed == "True":
        globVar.slow_speed = True
    else:
        globVar.slow_speed = False

def readPiecesArrays(save, c):
    wp_array = save.readline().split(',')
    k = 0
    if c == "W":
        globVar.w_pieces = []
        n = globVar.w_NumPieces
    else:
        globVar.b_pieces = []
        n = globVar.b_NumPieces
    for i in range(n):
        color = wp_array[k]
        k += 1
        selected = wp_array[k]
        if selected == "True":
            sl = True
        else:
            sl = False
        k += 1
        type = wp_array[k]
        k += 1
        label = int(wp_array[k])
        k += 1
        row = int(wp_array[k])
        k += 1
        col = int(wp_array[k])
        k += 1

        if type == "none":
            pc = pieces.Pawn("none", "none")
        elif type == "pawn":
            pc = pieces.Pawn(color, type)
        elif type == "rook":
            pc = pieces.Rook(color, type)
        elif type == "bishop":
            pc = pieces.Bishop(color, type)
        elif type == "queen":
            pc = pieces.Queen(color, type)
        elif type == "king":
            pc = pieces.King(color, type)
        elif type == "knight":
            pc = pieces.Knight(color, type)

        pc.selected = sl
        pc.label = label
        pc.row = row
        pc.col = col

        if c == "W":
            globVar.w_pieces.append(pc)
        else:
            globVar.b_pieces.append(pc)

def read_firstPawns(save):
    p_array = save.readline().split(',')
    k = 0
    n = globVar.firstPawnsNum

    for i in range(n):
        color = p_array[k]
        k += 1
        selected = p_array[k]
        if selected == "True":
            sl = True
        else:
            sl = False
        k += 1
        type = p_array[k]
        k += 1
        label = int(p_array[k])
        k += 1
        row = int(p_array[k])
        k += 1
        col = int(p_array[k])
        k += 1
        fm = p_array[k]
        if fm == "True":
            firstMove = True
        else:
            firstMove = False
        k += 1

        pc = pieces.Pawn(color, type)

        pc.selected = sl
        pc.label = label
        pc.row = row
        pc.col = col
        pc.firstMove = firstMove

        globVar.firstPawns.append(pc)
        board.Grid(row, col).piece.firstMove = firstMove
        index = findIndex(label, color)

        if color == "W" and index != None:
            globVar.w_pieces[index].firstMove = True
        elif color == "b" and index != None:
            globVar.b_pieces[index].firstMove = True

def read_r_avail(save):
    # read r_avail_array
    r_avail_array = save.readline().split(',')
    k = 0
    n = globVar.r_avail_Num
    for i in range(n):
        ps = r_avail_array[k]
        k += 1
        sqrColor = r_avail_array[k]
        k += 1
        pcColor = r_avail_array[k]
        k += 1
        type = r_avail_array[k]
        k += 1
        label = int(r_avail_array[k])
        k += 1
        p_row = int(r_avail_array[k])
        k += 1
        p_col = int(r_avail_array[k])
        k += 1
        row = int(r_avail_array[k])
        k += 1
        col = int(r_avail_array[k])
        k += 1

        pc = pieceConstructor(pcColor, type)

        pc.label = label
        pc.row = p_row
        pc.col = p_col

        sq = Square(ps, sqrColor, pc, row, col)

        globVar.r_avail.append(sq)

def read_r_PiecesArrays(save, c):
    wp_array = save.readline().split(',')
    k = 0
    if c == "W":
        globVar.r_w_pieces = []
        n = globVar.r_w_NumPieces
    else:
        globVar.r_b_pieces = []
        n = globVar.r_b_NumPieces
    for i in range(n):
        color = wp_array[k]
        k += 1
        selected = wp_array[k]
        if selected == "True":
            sl = True
        else:
            sl = False
        k += 1
        type = wp_array[k]
        k += 1
        label = int(wp_array[k])
        k += 1
        row = int(wp_array[k])
        k += 1
        col = int(wp_array[k])
        k += 1

        pc = pieceConstructor(color, type)

        pc.selected = sl
        pc.label = label
        pc.row = row
        pc.col = col

        if c == "W":
            globVar.r_w_pieces.append(pc)
        else:
            globVar.r_b_pieces.append(pc)

def read_p_moves(save):
    # read white pieces
    p_w_array = save.readline().split(',')
    k = 0
    n = globVar.p_w_Num
    for i in range(n):
        ps = p_w_array[k]
        k += 1
        sqrColor = p_w_array[k]
        k += 1
        pcColor = p_w_array[k]
        k += 1
        type = p_w_array[k]
        k += 1
        label = int(p_w_array[k])
        k += 1
        p_row = int(p_w_array[k])
        k += 1
        p_col = int(p_w_array[k])
        k += 1
        row = int(p_w_array[k])
        k += 1
        col = int(p_w_array[k])
        k += 1

        pc = pieceConstructor(pcColor, type)

        pc.label = label
        pc.row = p_row
        pc.col = p_col

        sq = Square(ps, sqrColor, pc, row, col)

        globVar.p_w_moves.append(sq)

    # read black pieces
    p_b_array = save.readline().split(',')
    k = 0
    n = globVar.p_b_Num
    for i in range(n):
        ps = p_b_array[k]
        k += 1
        sqrColor = p_b_array[k]
        k += 1
        pcColor = p_b_array[k]
        k += 1
        type = p_b_array[k]
        k += 1
        label = int(p_b_array[k])
        k += 1
        p_row = int(p_b_array[k])
        k += 1
        p_col = int(p_b_array[k])
        k += 1
        row = int(p_b_array[k])
        k += 1
        col = int(p_b_array[k])
        k += 1

        pc = pieceConstructor(pcColor, type)

        pc.label = label
        pc.row = p_row
        pc.col = p_col

        sq = Square(ps, sqrColor, pc, row, col)

        globVar.p_b_moves.append(sq)

def writeBoard(save):
    for i in range(8):
        for j in range(8):
            save.write(str(board.Grid(i,j).pieceStatus))
            save.write(",")
            save.write(str(board.Grid(i,j).color))
            save.write(",")
            save.write(str(board.Grid(i,j).row))
            save.write(",")
            save.write(str(board.Grid(i,j).col))
            save.write(",")
            save.write(str(board.Grid(i,j).des))
            save.write(",")
            save.write(str(board.Grid(i,j).option))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.type))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.color))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.selected))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.label))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.row))
            save.write(",")
            save.write(str(board.Grid(i,j).piece.col))
            save.write(",")

def writeGlobal(save):
    save.write("\n")
    save.write(str(globVar.numPlayers))
    save.write("\n")
    save.write(str(globVar.player))
    save.write("\n")
    save.write(str(globVar.noPlayers))
    save.write("\n")
    save.write(str(globVar.playerCount))
    save.write("\n")
    save.write(str(globVar.w_NumPieces))
    save.write("\n")
    save.write(str(globVar.b_NumPieces))
    save.write("\n")
    save.write(str(globVar.r_w_NumPieces))
    save.write("\n")
    save.write(str(globVar.r_b_NumPieces))
    save.write("\n")
    save.write(str(globVar.w_check))
    save.write("\n")
    save.write(str(globVar.b_check))
    save.write("\n")
    save.write(str(globVar.removed))
    save.write("\n")
    save.write(str(globVar.removed_label))
    save.write("\n")
    save.write(str(globVar.removed_color))
    save.write("\n")
    save.write(str(globVar.last_row))
    save.write("\n")
    save.write(str(globVar.last_col))
    save.write("\n")
    save.write(str(globVar.scanning))
    save.write("\n")
    save.write(str(globVar.r_avail_Num))
    save.write("\n")
    save.write(str(globVar.p_w_Num))
    save.write("\n")
    save.write(str(globVar.p_b_Num))
    save.write("\n")
    save.write(str(globVar.m_f_ps))
    save.write("\n")
    save.write(str(globVar.m_f_p_color))
    save.write("\n")
    save.write(str(globVar.m_f_p_type))
    save.write("\n")
    save.write(str(globVar.m_f_p_label))
    save.write("\n")
    save.write(str(globVar.m_f_row))
    save.write("\n")
    save.write(str(globVar.m_f_col))
    save.write("\n")
    save.write(str(globVar.m_t_ps))
    save.write("\n")
    save.write(str(globVar.m_t_p_color))
    save.write("\n")
    save.write(str(globVar.m_t_p_type))
    save.write("\n")
    save.write(str(globVar.m_t_p_label))
    save.write("\n")
    save.write(str(globVar.m_t_row))
    save.write("\n")
    save.write(str(globVar.m_t_col))
    save.write("\n")
    save.write(str(globVar.m_fm))
    save.write("\n")
    save.write(str(globVar.u_m_f_ps))
    save.write("\n")
    save.write(str(globVar.u_m_f_p_color))
    save.write("\n")
    save.write(str(globVar.u_m_f_p_type))
    save.write("\n")
    save.write(str(globVar.u_m_f_p_label))
    save.write("\n")
    save.write(str(globVar.u_m_f_row))
    save.write("\n")
    save.write(str(globVar.u_m_f_col))
    save.write("\n")
    save.write(str(globVar.u_m_t_ps))
    save.write("\n")
    save.write(str(globVar.u_m_t_p_color))
    save.write("\n")
    save.write(str(globVar.u_m_t_p_type))
    save.write("\n")
    save.write(str(globVar.u_m_t_p_label))
    save.write("\n")
    save.write(str(globVar.u_m_t_row))
    save.write("\n")
    save.write(str(globVar.u_m_t_col))
    save.write("\n")
    save.write(str(globVar.u_m_fm))
    save.write("\n")
    save.write(str(globVar.no_b_king))
    save.write("\n")
    save.write(str(globVar.no_w_king))
    save.write("\n")
    save.write(str(globVar.firstPawnsNum))
    save.write("\n")
    save.write(str(globVar.checkmate))
    save.write("\n")
    save.write(str(globVar.slow_speed))
    save.write("\n")

def writePiecesArrays(save):
    # save w_pieces
    for i in range(len(globVar.w_pieces)):
        save.write(str(globVar.w_pieces[i].color))
        save.write(",")
        save.write(str(globVar.w_pieces[i].selected))
        save.write(",")
        save.write(str(globVar.w_pieces[i].type))
        save.write(",")
        save.write(str(globVar.w_pieces[i].label))
        save.write(",")
        save.write(str(globVar.w_pieces[i].row))
        save.write(",")
        save.write(str(globVar.w_pieces[i].col))
        save.write(",")

    save.write("\n")

    # save b_pieces
    for i in range(len(globVar.b_pieces)):
        save.write(str(globVar.b_pieces[i].color))
        save.write(",")
        save.write(str(globVar.b_pieces[i].selected))
        save.write(",")
        save.write(str(globVar.b_pieces[i].type))
        save.write(",")
        save.write(str(globVar.b_pieces[i].label))
        save.write(",")
        save.write(str(globVar.b_pieces[i].row))
        save.write(",")
        save.write(str(globVar.b_pieces[i].col))
        save.write(",")

def write_r_PiecesArrays(save):
    save.write("\n")

    # save r_w_pieces
    for i in range(len(globVar.r_w_pieces)):
        save.write(str(globVar.r_w_pieces[i].color))
        save.write(",")
        save.write(str(globVar.r_w_pieces[i].selected))
        save.write(",")
        save.write(str(globVar.r_w_pieces[i].type))
        save.write(",")
        save.write(str(globVar.r_w_pieces[i].label))
        save.write(",")
        save.write(str(globVar.r_w_pieces[i].row))
        save.write(",")
        save.write(str(globVar.r_w_pieces[i].col))
        save.write(",")

    save.write("\n")

    # save r_b_pieces
    for i in range(len(globVar.r_b_pieces)):
        save.write(str(globVar.r_b_pieces[i].color))
        save.write(",")
        save.write(str(globVar.r_b_pieces[i].selected))
        save.write(",")
        save.write(str(globVar.r_b_pieces[i].type))
        save.write(",")
        save.write(str(globVar.r_b_pieces[i].label))
        save.write(",")
        save.write(str(globVar.r_b_pieces[i].row))
        save.write(",")
        save.write(str(globVar.r_b_pieces[i].col))
        save.write(",")

    save.write("\n")

    # save r_avail
    for i in range(len(globVar.r_avail)):
        save.write(str(globVar.r_avail[i].pieceStatus))
        save.write(",")
        save.write(str(globVar.r_avail[i].color))
        save.write(",")
        save.write(str(globVar.r_avail[i].piece.color))
        save.write(",")
        save.write(str(globVar.r_avail[i].piece.type))
        save.write(",")
        save.write(str(globVar.r_avail[i].piece.label))
        save.write(",")
        save.write(str(globVar.r_avail[i].piece.row))
        save.write(",")
        save.write(str(globVar.r_avail[i].piece.col))
        save.write(",")
        save.write(str(globVar.r_avail[i].row))
        save.write(",")
        save.write(str(globVar.r_avail[i].col))
        save.write(",")

    save.write("\n")

def write_firstPawns(save):
    recordFirstPawns()
    # save firstPawns
    for i in range(len(globVar.firstPawns)):
        save.write(str(globVar.firstPawns[i].color))
        save.write(",")
        save.write(str(globVar.firstPawns[i].selected))
        save.write(",")
        save.write(str(globVar.firstPawns[i].type))
        save.write(",")
        save.write(str(globVar.firstPawns[i].label))
        save.write(",")
        save.write(str(globVar.firstPawns[i].row))
        save.write(",")
        save.write(str(globVar.firstPawns[i].col))
        save.write(",")
        save.write(str(globVar.firstPawns[i].firstMove))
        save.write(",")

def write_p_moves(save):
    # white potenial moves
    for i in range(len(globVar.p_w_moves)):
        save.write(str(globVar.p_w_moves[i].pieceStatus))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].color))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].piece.color))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].piece.type))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].piece.label))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].piece.row))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].piece.col))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].row))
        save.write(",")
        save.write(str(globVar.p_w_moves[i].col))
        save.write(",")

    save.write("\n")

    # black potenial moves
    for i in range(len(globVar.p_b_moves)):
        save.write(str(globVar.p_b_moves[i].pieceStatus))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].color))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].piece.color))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].piece.type))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].piece.label))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].piece.row))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].piece.col))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].row))
        save.write(",")
        save.write(str(globVar.p_b_moves[i].col))
        save.write(",")

    save.write("\n")

def clearSave():
    save = open("chess.save","w")
    save.close()

def delete_save():
    if os.path.isfile("chess.save"):
        os.remove("chess.save")
    clearMovesHistory()

def clearMovesHistory():
    # file = open("moves.txt", "w")
    # file.close()
    if os.path.isfile("chess.save"):
        os.remove("moves.txt")

def hasMoves(availMoves):
    if len(availMoves) > 0:
        return True
    else:
        return False

def recordMove(fromSqr, toSqr):
    # record fromSqr
    globVar.m_f_ps = fromSqr.pieceStatus
    globVar.m_f_p_color = fromSqr.piece.color
    globVar.m_f_p_type = fromSqr.piece.type
    globVar.m_f_p_label = fromSqr.piece.label
    globVar.m_f_row = fromSqr.row
    globVar.m_f_col = fromSqr.col
    # record toSqr
    globVar.m_t_ps = toSqr.pieceStatus
    globVar.m_t_p_color = toSqr.piece.color
    globVar.m_t_p_type = toSqr.piece.type
    globVar.m_t_p_label = toSqr.piece.label
    globVar.m_t_row = toSqr.row
    globVar.m_t_col = toSqr.col

    if fromSqr.piece.type == "pawn":
        globVar.m_fm = fromSqr.piece.firstMove
        board.Grid(fromSqr.row, fromSqr.col).piece.firstMove = False

def record_user_move(fpc, availMoves, choice):
    toSqr = copy.deepcopy(availMoves[choice - 1])
    tpc = toSqr.piece
    file = open("moves.txt", "a+")
    file.write("Turn #{}\n".format(globVar.playerCount + 1))
    if globVar.player == "W":
        file.write("WHITE\n")
    else:
        file.write("BLACK\n")

    file.write(fpc.type + "\n")

    f_col = chr(fpc.col + 65)
    f_row = (8 - fpc.row)
    t_col = chr(tpc.col + 65)
    t_row = (8 - tpc.row)

    file.write(str(f_col) + str(f_row) + " ---> " + str(t_col) + str(t_row) + "\n\n")
    file.close()

    globVar.u_m_f_ps = board.Grid(fpc.row, fpc.col).pieceStatus
    globVar.u_m_f_p_color = fpc.color
    globVar.u_m_f_p_type = fpc.type
    globVar.u_m_f_p_label = fpc.label
    globVar.u_m_f_row = fpc.row
    globVar.u_m_f_col = fpc.col
    # record toSqr
    globVar.u_m_t_ps = board.Grid(tpc.row, tpc.col).pieceStatus
    globVar.u_m_t_p_color = tpc.color
    globVar.u_m_t_p_type = tpc.type
    globVar.u_m_t_p_label = tpc.label
    globVar.u_m_t_row = toSqr.row
    globVar.u_m_t_col = toSqr.col

    if fpc.type == "pawn":
        globVar.u_m_fm = fpc.firstMove
        board.Grid(fpc.row, fpc.col).piece.firstMove = False

def undo_user_move():
    # read and build fpc
    fSqr_status = globVar.u_m_f_ps
    f_clr = globVar.u_m_f_p_color
    f_type = globVar.u_m_f_p_type
    f_label = globVar.u_m_f_p_label
    f_row = globVar.u_m_f_row
    f_col = globVar.u_m_f_col
    fpc = pieceConstructor(f_clr, f_type)

    fpc.label = f_label
    fpc.row = f_row
    fpc.col = f_col

    # read and build tpc
    tSqr_status = globVar.u_m_t_ps
    t_clr = globVar.u_m_t_p_color
    t_type = globVar.u_m_t_p_type
    t_label = globVar.u_m_t_p_label
    t_row = globVar.u_m_t_row
    t_col = globVar.u_m_t_col
    tpc = pieceConstructor(t_clr, t_type)

    tpc.label = t_label
    tpc.row = t_row
    tpc.col = t_col

    if fpc.type == "pawn":
        fpc.firstMove = globVar.u_m_fm

    # update the board
    board.uGrid(fpc)
    board.uGrid(tpc)
    updatePieces(fpc)

    board.Grid(fpc.row, fpc.col).pieceStatus = fSqr_status
    board.Grid(tpc.row, tpc.col).pieceStatus = tSqr_status

    # reset des
    board.Grid(fpc.row, fpc.col).des = False
    board.Grid(tpc.row, tpc.col).des = False

    if not globVar.removed:
        board.Grid(tpc.row,tpc.col).pieceStatus = False
        board.Grid(tpc.row,tpc.col).piece.color = "none"

    un_deletePiece(fpc)
    globVar.removed = False
    board.Grid(fpc.row, fpc.col).piece.selected = True

def undoMove():
    # read and build fpc
    fSqr_status = globVar.m_f_ps
    f_clr = globVar.m_f_p_color
    f_type = globVar.m_f_p_type
    f_label = globVar.m_f_p_label
    f_row = globVar.m_f_row
    f_col = globVar.m_f_col
    fpc = pieceConstructor(f_clr, f_type)

    fpc.label = f_label
    fpc.row = f_row
    fpc.col = f_col

    # read and build tpc
    tSqr_status = globVar.m_t_ps
    t_clr = globVar.m_t_p_color
    t_type = globVar.m_t_p_type
    t_label = globVar.m_t_p_label
    t_row = globVar.m_t_row
    t_col = globVar.m_t_col
    tpc = pieceConstructor(t_clr, t_type)

    tpc.label = t_label
    tpc.row = t_row
    tpc.col = t_col

    if fpc.type == "pawn":
        fpc.firstMove = globVar.m_fm

    # update the board
    board.uGrid(fpc)
    board.uGrid(tpc)
    updatePieces(fpc)

    board.Grid(fpc.row, fpc.col).pieceStatus = fSqr_status
    board.Grid(tpc.row, tpc.col).pieceStatus = tSqr_status

    # reset des
    board.Grid(fpc.row, fpc.col).des = False
    board.Grid(tpc.row, tpc.col).des = False

    if not globVar.removed:
        board.Grid(tpc.row,tpc.col).pieceStatus = False
        board.Grid(tpc.row,tpc.col).piece.color = "none"

    un_deletePiece(fpc)
    globVar.removed = False
    board.Grid(fpc.row, fpc.col).piece.selected = True

def pieceConstructor(clr, type):
    if type == "none":
        pc = pieces.Pawn("none", "none")
    elif type == "pawn":
        pc = pieces.Pawn(clr, type)
    elif type == "rook":
        pc = pieces.Rook(clr, type)
    elif type == "bishop":
        pc = pieces.Bishop(clr, type)
    elif type == "queen":
        pc = pieces.Queen(clr, type)
    elif type == "king":
        pc = pieces.King(clr, type)
    elif type == "knight":
        pc = pieces.Knight(clr, type)
    return pc

def typeCounter(type, color):
    n = 0
    if color == "W":
        for i in range(len(globVar.w_pieces)):
            if globVar.w_pieces[i].type == type:
                n += 1

    else:
        for i in range(len(globVar.b_pieces)):
            if globVar.b_pieces[i].type == type:
                n += 1

    return n

def recordFirstPawns():
    globVar.firstPawnsNum = 0
    globVar.firstPawns = [pieces.Pawn("none", "none")]
    for i in range(8):
        for j in range(8):
            if (board.Grid(i,j).piece.type == "pawn" and
            board.Grid(i,j).piece.firstMove and
            board.Grid(i,j).piece.color != "none"):
                globVar.firstPawns.append(board.Grid(i,j).piece)
    globVar.firstPawnsNum = len(globVar.firstPawns)
