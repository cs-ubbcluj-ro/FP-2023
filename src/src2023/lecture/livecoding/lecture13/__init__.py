"""
Chomp

1. Draw the board with a nice header
2. Make a move on the board (with exception for validation)
3. The Computer player (plays randomly)
4. UI (human vs. computer)

How does layered architecture work in these games?
- the board represents the domain layer (we have a single entity and
a single object in the domain)
- the computer player replaces the services
https://refactoring.guru/design-patterns/strategy
- the UI maanges the flow of the game
"""