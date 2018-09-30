"""
This module contains functions that display text to the screen, such as error
messages and the game board.
"""

import os
import platform
import random
import board
import globVar
import sys
import utils

def drawBoard():
    clear()

    nowPlaying()

    numLabel = 8
    letterLabel = 'A'

    print("\n     ", end = "")
    for i in range(8):
        print(letterLabel + " ", end = "")
        letterLabel = chr(ord(letterLabel) + 1)

    print("\n    ",end="")
    for i in range(18):
        print("_",end="")

    print("\n", end = "")
    for i in range(8):
        print(' {}  |'.format(numLabel), end = "")
        for j in range(8):
            print(board.Grid(i, j), end = "")
        print("|",end="")
        numLabel -= 1
        print("\n", end = "")
    print("    ",end="")
    for i in range(18):
        print("¯",end="")
    print("\n",end="")

    remaining()

def nowPlaying():
    print(" ",end="")
    for i in range(23):
        print("-",end="")
    if( (globVar.w_check and globVar.player == "W") or
    (globVar.b_check and globVar.player == "b")):
        print("\n |       CHECK!    ", globVar.player, " |")
    elif globVar.checkmate:
        print("\n |      CHECKMATE!     |")
    else:
        print("\n |    NOW PLAYING: ", globVar.player, " |")
    print(" ",end="")
    for i in range(23):
        print("-",end="")

def pawn_to_new():
    drawBoard()
    while True:
        try:
            print(" 1. Rook    2. Knight")
            print(" 3. Bishop  4. Queen")
            choice = input("\n Choose a new piece: ")
            choices(choice)
        except ValueError:
            pawnError()
            continue
        if (choice == "" or len(choice) > 1 or not choice.isdigit()
        or int(choice) < 1 or int(choice) > 4):
            pawnError()
            continue
        else:
            break
    return int(choice)

def remaining():
    w_pawn_count = utils.typeCounter("pawn", "W")
    w_rook_count = utils.typeCounter("rook", "W")
    w_knight_count = utils.typeCounter("knight", "W")
    w_bishop_count = utils.typeCounter("bishop", "W")
    w_queen_count = utils.typeCounter("queen", "W")
    w_king_count = utils.typeCounter("king", "W")
    b_pawn_count = utils.typeCounter("pawn", "b")
    b_rook_count = utils.typeCounter("rook", "b")
    b_knight_count = utils.typeCounter("knight", "b")
    b_bishop_count = utils.typeCounter("bishop", "b")
    b_queen_count = utils.typeCounter("queen", "b")
    b_king_count = utils.typeCounter("king", "b")

    print(" ",end="")
    print("       REMAINING:\n ", end="")
    for i in range(23):
        print("_",end="")
    print("\n   White:   |   Black:")
    print("  {}P'  {}R'  |  {}p.  {}r.".format(w_pawn_count, w_rook_count, b_pawn_count, b_rook_count))
    print("  {}N'  {}B'  |  {}n.  {}b.".format(w_knight_count, w_bishop_count, b_knight_count, b_bishop_count))
    print("  {}Q'  {}K'  |  {}q.  {}k.".format(w_queen_count, w_king_count, b_queen_count, b_king_count))

    print(" ",end="")
    for i in range(23):
        print("¯",end="")
    print("\n")

def startScreen():
    while True:
        try:
            clear()
            print("\n Welcome to Chess: Python Edition!\n\n")
            n = input(" How many players for this game?\n (0, 1, or 2): ")

        except ValueError:
            print("\n Please choose an option.")
            print("\n Press Enter to continue.")
            input("")
            continue

        if (not n.isdigit()) or (int(n) < 0) or (int(n) > 2):
            print("\n Please choose an option.")
            print("\n Press Enter to continue.")
            input("")
            continue
        else:
            break

    globVar.numPlayers = int(n)

    if globVar.numPlayers < 2:
        random.seed(a=None)
    if globVar.numPlayers == 0:
        globVar.noPlayers = True
        speedMenu()

    board.populate()

    return True

def speedMenu():
    while True:
        try:
            clear()
            print("\n At what speed would you like the AI to play?")
            print("\n 1. Slow enough to watch the game")
            print(" 2. Full speed ahead")
            n = input("\n Option: ")
            choices(n)
        except ValueError:
            print("\n Please choose an option.")
            print("\n Press Enter to continue.")
            input("")
            continue

        if (not n.isdigit()) or (int(n) < 1) or (int(n) > 2):
            print("\n Please choose an option.")
            print("\n Press Enter to continue.")
            input("")
            continue
        else:
            break

    if int(n) == 1:
        globVar.slow_speed = True
    else:
        globVar.slow_speed = False

def chooseAvailableMessage():
    errorSeparator()
    print("\n Please choose a piece with available moves.")
    pressEnter()

def getouttacheckMessage():
    errorSeparator()
    print("\n Choose a move to get out of check.")
    pressEnter()

def pickValidMoveMessage():
    errorSeparator()
    print("\n Please pick a valid move.")
    pressEnter()

def pawnError():
    errorSeparator()
    print("\n Please pick a valid piece.")
    pressEnter()

def pressEnter():
    print(" Press Enter to continue.")
    input("")
    drawBoard()

def selectError():
    errorSeparator()
    print("\n Please choose a square with one of your pieces.")
    pressEnter()

def colError():
    errorSeparator()
    print("\n Please choose a valid column.")
    pressEnter()

def rowError():
    errorSeparator()
    print("\n Please choose a valid row.")
    pressEnter()

def errorSeparator():
    print("\n ",end="")
    for i in range(43):
        print("-",end="")

def clear():
    if platform.system() == "Linux":
        os.system("clear")
    if platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("CLS")
    else:
        print("\033c")

def chooseCol():
    while True:
        try:
            choice = input("\n Choose a column (letter): ")
            choices(choice)
        except ValueError:
            colError()
            continue
        if (choice == "" or len(choice) > 1 or
        ord(choice.upper()) < ord('A') or ord(choice.upper()) > ord('H')):
            colError()
            continue
        else:
            break
    return choice

def chooseRow():
    while True:
        try:
            choice = input("\n Choose a row (number): ")
            choices(choice)
        except ValueError:
            rowError()
            continue

        if not choice.isdigit() or choice == "":
            rowError()
            continue

        elif int(choice) < 1 or int(choice) > 8:
            rowError()
            continue
        else:
            break

    return int(choice)

def chooseMove(availMovesL):
    while True:
        try:
            choice = input("\n Choose a move (number): ")
            choices(choice)
        except ValueError:
            pickValidMoveMessage()
            continue

        if not choice.isdigit() or choice == "":
            pickValidMoveMessage()
            continue

        elif (int(choice) < 1) or (int(choice) > availMovesL):
            pickValidMoveMessage()
            continue
        else:
            break

    return int(choice)

def choices(choice):
    if choice.upper() == "Q":
        quit()
    elif choice.upper() == "R":
        board.populate()
        clear()
        print("\n The board has been reset.")
        pressEnter()
    elif choice.upper() == "L":
        utils.readSave()
        clear()
        print("\n The last save has been loaded.")
        pressEnter()

def quit():
    clear()
    print("\n Would you like to save your game? ", end="")
    y = yesNo()
    clear()
    if y:
        utils.writeSave()
    else:
        utils.delete_save()
    sys.exit(0)

def yesNo():
    y = input("(y/n): ")
    if (y.upper() == "Y" or y.upper() == "YES"):
        return True
    else:
        return False

def loadSave():
    clear()
    print("\n Save detected. Load previous game? ", end="")
    y = yesNo()
    if y:
        board.populate()
        utils.readSave()
    else:
        # board.populate()
        startScreen()
