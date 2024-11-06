from functools import reduce
from operator import mul
import itertools
class KenKenPuzzle:
    def __init__(self, size, cages):

        self.size = size  # Size of the NxN grid
        self.grid = [[0 for _ in range(size)] for _ in range(size)]  # Empty grid
        self.cages = cages  # List of cage constraints

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) if cell != 0 else "." for cell in row))
        print()


    def place_number(self, row, col, number):
        if(number<= self.size and row <= self.size and col <= self.size):
            self.grid[row][col] = number


    def check_cages(self):
        for cage in self.cages:
            cells = cage["cells"]
            values = [self.grid[r][c] for r, c in cells]

            if 0 in values:  # Skip cages that have empty cells
                continue

            if cage["operation"] == "+":
                if sum(values) != cage["target"]:
                    return False
            elif cage["operation"] == "x":
                if reduce(mul, values) != cage["target"]:
                    return False
            elif cage["operation"] == "-":
                valid = any(permutation[0] - sum(permutation[1:]) == cage["target"] for permutation in itertools.permutations(values))
                if not valid:
                    return False
            elif cage["operation"] == "%":
                valid = any(reduce(lambda x, y: x / y, permutation) == cage["target"] for permutation in itertools.permutations(values))
                if not valid:
                    return False
            else:
                return False  # If none of the conditions matched, cage is invalid

        return True

    def is_valid_grid(self):
        # Check each row for unique values
        for row in self.grid:
            if not self._has_unique_values(row):
                return False

        # Check each column for unique values
        for col in range(self.size):
            column_values = [self.grid[row][col] for row in range(self.size)]
            if not self._has_unique_values(column_values):
                return False

        return True

    def _has_unique_values(self, values):
        # Filter out zeros (unfilled cells) before checking uniqueness
        filtered_values = [v for v in values if v != 0]
        return len(filtered_values) == len(set(filtered_values))


# Sample 4x4 grid with placeholder cages
size = 4
cages = [
    {"target": 9, "operation": "+", "cells": [(0, 0), (0, 1),(0,2)]},
    {"target": 3, "operation": "-", "cells": [(1, 0), (1, 1)]},
]

puzzle = KenKenPuzzle(size, cages)
    
puzzle.place_number(0, 0, 1)
puzzle.place_number(0, 1, 4)  # Can now place same number in the row/column
puzzle.place_number(0, 2, 4)
puzzle.place_number(1, 0, 4)
puzzle.place_number(1, 1, 1)
puzzle.place_number(1, 2, 3)

puzzle.print_grid()
is_valid = puzzle.check_cages()
is_unique = puzzle.is_valid_grid()
print(is_valid)
print(is_unique)
#test 