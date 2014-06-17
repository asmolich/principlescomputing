"""
Clone of 2048 game.
"""
from random import randint
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    summable = False
    idx = 0
    lst = [0] * len(line)
    for elem in line:
        if elem > 0:
            if summable and lst[idx-1] == elem:
                lst[idx-1] <<= 1
                summable = False
            else:
                lst[idx] = elem
                idx += 1
                summable = True
    return lst

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.moves = 0
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid = [[0] * self.grid_width for dummy_row in range(self.grid_height)]

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0] * self.grid_width for dummy_row in range(self.grid_height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        zipped = zip(*self.grid)
        if direction == UP or direction == DOWN:
            for col in range(self.grid_width):
                merged = merge(zipped[col]) if direction == UP else merge(zipped[col][::-1])[::-1]
                if list(zipped[col]) != merged:
                    for idx in range(len(merged)):
                        self.grid[idx][col] = merged[idx]
                    moved = True
        else:
            for row in range(self.grid_height):
                merged = merge(self.grid[row]) if direction == LEFT else merge(self.grid[row][::-1])[::-1]
                if self.grid[row] != merged:
                    self.grid[row] = merged
                    moved = True
        if moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        self.moves += 1
        #value = 4 if self.moves % 10 == 0 else 2
        value = 4 if randint(1, 10) == 5 else 2
        posx = randint(0, self.grid_width - 1)
        posy = randint(0, self.grid_height - 1)
        #dist = 0
        while self.get_tile(posy, posx) > 0:
            posx = randint(0, self.grid_width - 1)
            posy = randint(0, self.grid_height - 1)
            #dist += 1
            #neighbours = [[(a,b) if abs(posy - a) % self.grid_width + abs(posx - b) % self.grid_height == dist
            #        or abs(posy - a + self.grid_width) % self.grid_width + abs(posx - b + self.grid_height) % self.grid_height == dist
            #        else None for b in range(4)] for a in range(4)]
            #for x, y in neighbours
        self.set_tile(posy, posx, value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

