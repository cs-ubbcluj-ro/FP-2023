"""
UI module for game

user commands:
    play 1,1  # plays in the center of the board
    takeback  # undo the user's last move
    exit
"""
from board import Board, GameWonException, BoardFullException
from game import Game


class UI:

    def help_user(self):
        print(
            """
            play 1, 1  # plays in the center of the board
            takeback  # undo the user's last move
            exit
            """)

    def _process_user_command(self, user_command):
        """
        Return user's command and its parameters
        :param user_command:
        :return:
        """
        user_command = user_command.strip()
        tokens = user_command.split(" ", maxsplit=1)
        command = tokens[0]

        if len(tokens) == 1:
            return command, ""

        tokens = tokens[1].split(",")
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()

        return command, tokens

    def start(self):
        game = Game()
        self.help_user()

        while True:
            print(game.get_board())
            user_command = input(">")
            command, params = self._process_user_command(user_command)

            if command == 'play':
                try:
                    row = int(params[0])
                    col = int(params[1])
                    game.human_move(row, col)
                except ValueError as ve:
                    print(str(ve))
                except BoardFullException:
                    print("-= Game Over. It's a draw! =-")
                    print(game.get_board())
                    return
                except GameWonException:
                    print("-= Congratulations! =-")
                    print(game.get_board())
                    return
                else:
                    try:
                        pos = game.computer_move()
                        print("Computer moved at " + str(pos))
                    except GameWonException:
                        print("-= Comiserations! =-")
                        print(game.get_board())
                        return
            elif command == 'takeback':
                pass
            elif command == 'exit':
                return
            else:
                print("Valid commands are:")
                self.help_user()


if __name__ == "__main__":
    ui = UI()
    ui.start()
