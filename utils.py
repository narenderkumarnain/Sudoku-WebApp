# This script contains functions for conversion of sudoku grid to Styled HTML Tables
# Author: @narenderkumarnain

# ---------------------------------Functions for Styling ---------------------------------------------------------------
#Conversion of Grid to Table with specific Colour
def list_to_table(list_str , color_input):
    res = '<center><table style="border-collapse: collapse;border: 1px solid black;padding: 5px;">'
    for i in range(len(list_str)):
        res += '<tr style="border-collapse: collapse;border: 1px solid black;padding: 5px;">'
        for j in range(len(list_str[i])):
            color = color_input
            if(list_str[i][j] == 0):
                color = "red"
            res += '<td style="border-collapse: collapse;' +'background:' + color + ';' + 'border: 1px solid black;padding: 5px 10px 5px 10px;">' + str(list_str[i][j]) + '</td>'
        res += '</tr>'
    res += '</table></center>'
    return res

# Wrapper function for Decomposition and recombination of Sudoku Sub-grids
def list_to_table_styled(grid):
    # Mannual division of the 3*3 Sub Grids
    grid1 = []
    grid1.append(
        [
            [ grid[0][0] , grid[0][1] , grid[0][2] ] ,
            [ grid[1][0] , grid[1][1] , grid[1][2] ] ,
            [ grid[2][0] , grid[2][1] , grid[2][2] ]
        ]
    )
    grid1.append(
        [
            [grid[0][3], grid[0][4], grid[0][5]],
            [grid[1][3], grid[1][4], grid[1][5]],
            [grid[2][3], grid[2][4], grid[2][5]]
        ]
    )
    grid1.append(
        [
            [grid[0][6], grid[0][7], grid[0][8]],
            [grid[1][6], grid[1][7], grid[1][8]],
            [grid[2][6], grid[2][7], grid[2][8]]
        ]
    )

    grid2 = []
    grid2.append(
        [
            [grid[3][0], grid[3][1], grid[3][2]],
            [grid[4][0], grid[4][1], grid[4][2]],
            [grid[5][0], grid[5][1], grid[5][2]]
        ]
    )
    grid2.append(
        [
            [grid[3][3], grid[3][4], grid[3][5]],
            [grid[4][3], grid[4][4], grid[4][5]],
            [grid[5][3], grid[5][4], grid[5][5]]
        ]
    )
    grid2.append(
        [
            [grid[3][6], grid[3][7], grid[3][8]],
            [grid[4][6], grid[4][7], grid[4][8]],
            [grid[5][6], grid[5][7], grid[5][8]]
        ]
    )

    grid3 = []
    grid3.append(
        [
            [grid[6][0], grid[6][1], grid[6][2]],
            [grid[7][0], grid[7][1], grid[7][2]],
            [grid[8][0], grid[8][1], grid[8][2]]
        ]
    )
    grid3.append(
        [
            [grid[6][3], grid[6][4], grid[6][5]],
            [grid[7][3], grid[7][4], grid[7][5]],
            [grid[8][3], grid[8][4], grid[8][5]]
        ]
    )
    grid3.append(
        [
            [grid[6][6], grid[6][7], grid[6][8]],
            [grid[7][6], grid[7][7], grid[7][8]],
            [grid[8][6], grid[8][7], grid[8][8]]
        ]
    )
    main_res = '<table>'
    main_res += '<tr>' + '<td>' + list_to_table(grid1[0] , 'skyblue') + '</td>' + '<td>' + list_to_table(grid1[1] , 'lightgrey') +'</td>' + '<td>'  +  list_to_table(grid1[2] , 'lightgreen') + '</td>' + '</tr>'
    main_res += '<tr>' + '<td>' + list_to_table(grid2[0], 'lightyellow') + '</td>' +'<td>' +list_to_table(grid2[1], 'skyblue') + '</td>' +'<td>' +list_to_table(grid2[2], 'lightyellow') + '</td>' +'</tr>'
    main_res += '<tr>' + '<td>' +list_to_table(grid3[0], 'lightgreen') +'</td>' +'<td>' + list_to_table(grid3[1], 'lightgrey') +'</td>' +'<td>' + list_to_table(grid3[2], 'skyblue') + '</td>' +'</tr>'
    main_res += '</table>'
    return main_res


# ------------------------------ Code for Testing ----------------------------------------------------------------------
# For testing the functions
# sudo_input = []
# for i in range(9):
#     temp = []
#     for j in range(9):
#         temp.append(str(i) + ',' + str(j))
#     sudo_input.append(temp)
#
# html = list_to_table_styled(sudo_input)
# with open('trial.html' , 'w') as f:
#     f.write(html)