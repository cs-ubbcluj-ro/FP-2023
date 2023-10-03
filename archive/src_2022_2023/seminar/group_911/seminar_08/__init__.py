"""
Turning seminar 7 game into object-oriented representation

1. Let's turn the board module functions into the Board class
    How can we protect class attributes from outside changes?

    protecting class attributes from outside change:
        C#, Java, Kotlin, C++ -> public, protected, private (keywords)
        public -> anyone can access and change
        private -> only class functions can access and change
        protected -> only class functions and derived classes can access and change
        (default)

        Python
        <var. name> -> public
        _<var. name> -> private (convention)
        __<var. name> -> private (convention!?, name mangling)

    a. Created the game_board class
    b. changed create_board to __init__
    c. changed str_board to __str__
    d. added remaining methods to class
    e. shortened their names as it makes more sense
        (e.g., make_move_on_board -> move)
    f. rewrote test_board to work with class

2. Let's do the same to the game module
    a. Create the game class and add the board as a constructor parameter
    b. Add the *_move methods into the class
    c. Update them to use the private __board attribute

3. Update the UI module
4. Added the skynet_level_2 random move strategy :)
"""
