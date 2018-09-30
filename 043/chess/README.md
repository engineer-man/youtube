# Chess
This is a text-based version of Chess written in Python.

Use `python3 main.py` to run, or run the .exe I compiled for Windows (check the releases tab).

**Features:**
- Autosaves your progress
- Outputs each turn to a .txt file
- Prevents players from entering check
- Easy-to-use input
- Can be paused/quit and resumed
- Displays the remaining number of pieces on the board
- Exchange pawns for other pieces when reaching the other side of the board
- 0, 1, or 2 player modes

This project demonstrates inheritance by using six types of pieces, each with
its own scan() function. The program tracks players' remaining moves and pieces
and populates an array of potential moves after each turn. Once the list of
potential moves reaches zero, checkmate is called and the game ends.

I should have caught most bugs! Let me know how you break my code.

**Bugs:**
- None* at the moment

**To be implemented:**
- Castling
