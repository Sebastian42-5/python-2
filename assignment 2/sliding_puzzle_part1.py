import random

def tileLables(n):
    str_lst = []
    for i in range(1, n**2):
        str_lst.append(str(i))
    str_lst.append('  ')

    return str_lst

# display board function provided 


def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))
        
        

def getNewPuzzle(n):
    puzzle = []
    lines = tileLables(n)
    random.shuffle(lines)
    for i in range(n):
        line = lines[ i * n: (i + 1) * n]
        puzzle.append(line)
    puzzle = displayBoard(puzzle)
    
    return puzzle

print(getNewPuzzle(3))


def findEmptyTile(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])

    for i in range(rows):
        for j in range(columns):
            if puzzle[i][j] == '  ':
                empty_coord = (i, j)
    return empty_coord


# def nextMove(puzzle):
#     move = input('Enter your move: ')

#     if move == 'W':
    
#     elif move == 'A':

#     elif move == 'S':
    
#     elif move == 'D':

    
    









