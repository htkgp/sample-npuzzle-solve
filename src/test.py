from problem import PuzzleSolver
from puzzleGenerator import puzzle_generator
# basic test
UP = 3
DOWN = 1
RIGHT = 2
LEFT = 0
test_puzzle = \
    [[3, 1, 2],
    [6, 5, 8],
    [7, 0, 4]]
test_puzzle = puzzle_generator(8)
t = PuzzleSolver(test_puzzle)
a = t.a_star()
t.show_text_frame(a)
# t.output_visualize(a)
