from extractor import sudoku_extractor
from solver import backtrack
import time

def solve(img_path):
    model_path = 'extractor/myModel.h5'
    start = time.time()
    board = sudoku_extractor.extract_sudoku(img_path , model_path)
    if(board == None):
        print('Sudoku not found')
        return []
    end1 = time.time()

    board_list = []
    for i in range(9):
        board_list.append(list(board[i]))

    for i in range(9):
        print(board_list[i])
    grid_res = backtrack.sudoku_solver(board_list , 9)
    if(grid_res == None):
        print('not solvable')
        return board_list
    end2 = time.time()
    print('Time: {} {} {}'.format(start , end1 , end2))
    return grid_res
    # for i in range(9):
    #     print(grid_res[i])

#solve('examples/sudoku5.png')

