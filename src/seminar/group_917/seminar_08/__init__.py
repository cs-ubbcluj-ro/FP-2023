"""
1. Transform the functions in board module into a board class
    How do we protect the game_board from outside access/changes?
        -> in C++/Java/C#
        public - you can access it from anywhere
        protected - you can access it from inside the class and inherited classes
        private - access is allowed only from within the class

        -> Python
        <name> - public # e.g., game_board.board
        _<name> - private (convention) # e.g., game_board._board
        __<name> - private (convention!?, name mangling)
                        # e.g., game_board.__board
    a. Transform create_board into __init__
    b. Transform str_board into __str__
    c. Add remaining methods to class and update
    d. Update test case


"""
