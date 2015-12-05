class Board(object):
    """A game board"""

    # track spaces individually, or keep in list?
    spaces = []


    def __init__(self):
        """Makes spaces for new boards"""

        location = 0

        for num1 in range(-1, 2):
            for num2 in range(-1, 2):
                print location, " at: ", num1, num2
                space = Space(num1, num2, location)
                self.spaces.append(space)
                location += 1


    def available_spaces(self):
        """Returns list of open spaces"""

        available_spaces = []
        for space in self.spaces:
            if space.player == 0:
                available_spaces.append(space)

        return available_spaces


    def is_won(self):
        """Checks whether a player has won"""
        pass


    def winning_move(self, player):
        """Checks whether there is a winning move available for a given player"""
        pass

    def print_board(self):
        """Prints board to screen"""

        print self.spaces[2].player, "||", self.spaces[5].player, "||", self.spaces[8].player 
        print "==========="    
        print self.spaces[1].player, "||", self.spaces[4].player, "||", self.spaces[7].player
        print "==========="
        print self.spaces[0].player, "||", self.spaces[3].player, "||", self.spaces[6].player        


class Space(object):
    """A space on the game board"""

    player = 0


    def __init__(self, x, y, location):
        """Sets coordinates of new space"""

        self.x = x
        self.y = y
        self.location = location


    def __repr__(self):
        """Shows coordinates when object printed"""

        # return "(%s, %s)" % (self.x, self.y) 
        return "%s" % self.location


if __name__ == "__main__":

    board = Board()
    board.spaces[0].player = 1
    board.spaces[4].player = 2
    board.spaces[1].player = 1
    board.spaces[5].player = 2
    board.spaces[2].player = 1

