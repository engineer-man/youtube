"""
This is the main module for my chess game.
"""


import random
import Canvas
import utils
import board
import Player
import globVar
import pathlib

def main():
    path = pathlib.Path("chess.save")
    if path.exists():
        Canvas.loadSave()
        running = True
    else:
        running = Canvas.startScreen()

    while(running):
        running = state()

    utils.delete_save()


def state():

    playing = True

    while playing:
        if (globVar.playerCount % 2) == 0:
            globVar.player = "W"
        else:
            globVar.player = "b"

        Player.turn()
        globVar.playerCount += 1
        # utils.check_king()
        playing = not utils.checkWin()
        utils.clearSave()
        utils.writeSave()

    return playing



if __name__ == "__main__":
    main()
