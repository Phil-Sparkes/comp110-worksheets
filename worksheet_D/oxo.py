class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.gameboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        square = x + y * 3
        return self.gameboard[square]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        square = x + y * 3
        if self.gameboard[square] == 0:
            self.gameboard[square] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        test = 0
        for squares in xrange(9):
            if self.gameboard[squares] == 0:
                test += 1
                return False

        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for x in xrange(3):

            # Checks for horizontal and vertical lines of 3
            if self.gameboard[x] == self.gameboard[x+3] and self.gameboard[x+3] == self.gameboard[x+6]:
                return self.gameboard[x]
            if self.gameboard[x*3] == self.gameboard[x*3+1] and self.gameboard[x*3+1] == self.gameboard[x*3+2]:
                return self.gameboard[x*3]

        # Checks for diagonal lines of 3
        if self.gameboard[0] == self.gameboard[4] and self.gameboard[4] == self.gameboard[8]:
            return self.gameboard[0]
        if self.gameboard[2] == self.gameboard[4] and self.gameboard[4] == self.gameboard[6]:
            return self.gameboard[2]

        return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        print board.gameboard
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                board.show()
                print "Player", winner, "wins!"
                break   # End the game

            elif board.is_board_full():
                board.show()
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
