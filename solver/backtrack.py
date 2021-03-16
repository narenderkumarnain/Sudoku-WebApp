# BackTracking based Sudoku Solver
# May 16, 2021 22:40 IST
# Author: @narenderkumarnain

import math


def CanPlace(grid, N, i, j, n):
    # can we place the number n in this cell ?
    for k in range(N):
        if (grid[i][k] == n) or (grid[k][j] == n):
            return False

    rn = math.sqrt(N)
    sx = int(i / rn) * rn
    sy = int(j / rn) * rn

    for x in range(int(sx), int(sx + rn)):
        for y in range(int(sy), int(sy + rn)):
            if (x != i and y != j) and (grid[x][y] == n):
                return False

    return True


def recursion_solver(grid, N, i, j):
    # base cases
    if j == N:
        return recursion_solver(grid, N, i + 1, 0)
    if i == N:
        return True
    if (grid[i][j] != 0):
        # prefilled cell
        return recursion_solver(grid, N, i, j + 1)

    for k in range(1, N + 1):
        if CanPlace(grid, N, i, j, k) == True:
            grid[i][j] = k
            future_res = recursion_solver(grid, N, i, j + 1)
            if future_res == True:
                return True

    grid[i][j] = 0
    return False


def sudoku_solver(grid, N):
    if len(grid) != N:
        raise Exception()
    for tmp in grid:
        if len(tmp) != N:
            raise Exception()
    # calling main recursion solver
    return recursion_solver(grid, N, 0, 0)

# tesing the sudoku_solver function here
# it worked out
# grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
#          [5, 2, 0, 0, 0, 0, 0, 0, 0],
#          [0, 8, 7, 0, 0, 0, 0, 3, 1],
#          [0, 0, 3, 0, 1, 0, 0, 8, 0],
#          [9, 0, 0, 8, 6, 3, 0, 0, 5],
#          [0, 5, 0, 0, 9, 0, 6, 0, 0],
#          [1, 3, 0, 0, 0, 0, 2, 5, 0],
#          [0, 0, 0, 0, 0, 0, 0, 7, 4],
#          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
#
# sudoku_solver(grid , 9)
#
# for i in range(9):
#     print(grid[i])
