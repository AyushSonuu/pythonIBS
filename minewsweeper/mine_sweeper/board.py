from cell import Cell
from level import Level


class Board:
    """
    Board class creates a 2D array of Cell type which represents the game board.

    Attributes:
    - board (list): 2D list of Cell instances representing the game board.

    Author: Ayush
    """

    def __init__(self, lev: Level):
        """
        Constructor for the Board class.

        Parameters:
        - lev (Level): The difficulty level of the game.
        """
        self.board = self.initialize_array(lev.rows, lev.cols)

    def get_board(self) -> list:
        """
        Returns the 2D array representing the game board.

        Returns:
        - list: 2D list of Cell instances representing the game board.
        """
        return self.board

    def initialize_array(self, rows: int, cols: int) -> list:
        """
        Initializes the 2D array representing the game board with Cell instances.

        Parameters:
        - rows (int): Number of rows in the game board.
        - cols (int): Number of columns in the game board.

        Returns:
        - list: 2D list of Cell instances representing the game board.
        """
        arr = []
        for i in range(rows):
            row = []
            for j in range(cols):
                c = Cell()
                row.append(c)
            arr.append(row)
        return arr
