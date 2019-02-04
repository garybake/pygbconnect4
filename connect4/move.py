class Move():
    """
    User can choose which column to play

    Move.play(col)
    """
    def __init__(self, col=None):
        assert col is not None
        self.col = col

    @classmethod
    def play(cls, col):
        """
        Places a stone on the board
        """
        return Move(col=col)