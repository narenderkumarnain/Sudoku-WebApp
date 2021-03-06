# Wrapper functions for Sudoku Extraction and Solver
# Author: @narenderkumarnain


from extractor import sudoku_extractor
from solver import backtrack
import time

def solve(img_path):
    # Path of the Tensorflow Digit Recognition Model
    # Change this to your Requirements
    model_path = 'extractor/myModel.h5'
    start = time.time()
    board = sudoku_extractor.extract_sudoku(img_path , model_path)
    if(board == None):
        print('Sudoku not found')
        return False , []
    end1 = time.time()

    board_list = []
    for i in range(9):
        board_list.append(list(board[i]))

    for i in range(9):
        print(board_list[i])
    grid_res = backtrack.sudoku_solver(board_list , 9)
    if(grid_res == None):
        print('not solvable')
        return False , board_list
    end2 = time.time()
    print('Time: {} {}'.format(end1 - start , end2 - start))
    return True , grid_res


#solve('examples/sudoku5.png')

