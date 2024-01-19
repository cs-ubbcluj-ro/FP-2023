"""
How do we implement layered architecture in a game?

UI
    - displays the state of the game (board)
    - read the human player's input
    - manages the sequence of moves

Services --> Game class where it makes sense
    - manage the human player's moves
    - determine where the computer should play

Repository
    - provide persistance to the program (save to files)
    - save the state of the game to a file (save/load game)

Domain
    - can be the game board (ex. Tic Tac Toe, Battleship, Minesweeper)
    - some other class (ex. Cows and Bulls)
"""