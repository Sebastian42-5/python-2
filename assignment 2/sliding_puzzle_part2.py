# part 1 of the assignment 2:

import random
import sys 

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
        line = lines[i * n: (i + 1) * n]
        puzzle.append(line)
    
    return puzzle

# print(getNewPuzzle(3))


def findEmptyTile(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])

    for i in range(rows):
        for j in range(columns):
            if puzzle[i][j] == '  ':
                empty_coord = (i, j)
    return empty_coord


def nextMove(puzzle):
    move_lst = ['W', 'A', 'S', 'D', 'quit']

    rows = len(puzzle)
    columns = len(puzzle[0])

    empty_row, empty_column = findEmptyTile(puzzle)

    valid_moves = ['quit']

    if empty_row > 0: 
        valid_moves.append('S')  # you can move up
    if empty_row < rows - 1: 
        valid_moves.append('W') # you can move down
    if empty_column > 0: 
        valid_moves.append('D') # you can move left
    if empty_column < columns - 1:
        valid_moves.append('A') # you can move right

    move = ' '

    while move not in valid_moves: 
        move = input(f'Enter WASD (or QUIT) {'/'.join(valid_moves)}: ')
        if move not in valid_moves:
            print('You have an invalid input. Try again')

    if move == 'quit':
        sys.exit()


    return move 


# part 2 of the assignment 2:

# Sebastian Soto 2432947

# 5.

def makeMove(puzzle, move):

    empty_row, empty_column = findEmptyTile(puzzle) 

    if move == 'W':
        puzzle[empty_row][empty_column], puzzle[empty_row + 1][empty_column] = puzzle[empty_row + 1][empty_column], puzzle[empty_row][empty_column]
    
    elif move == 'A':
        puzzle[empty_row][empty_column], puzzle[empty_row][empty_column + 1] = puzzle[empty_row][empty_column + 1], puzzle[empty_row][empty_column]
        

    elif move == 'S':
        puzzle[empty_row][empty_column], puzzle[empty_row - 1][empty_column] = puzzle[empty_row - 1][empty_column], puzzle[empty_row][empty_column]
        

    elif move == 'D':
        puzzle[empty_row][empty_column], puzzle[empty_row][empty_column - 1] = puzzle[empty_row][empty_column - 1], puzzle[empty_row][empty_column]
       
    return None


# helping function to determine if the player won or not:

def puzzleWin(puzzle):

    n = len(puzzle)

    correct_order = [str(i) for i in range(1, n**2)] + ['  ']

    flat_puzzle = [tile for row in puzzle for tile in row]
        
    return flat_puzzle == correct_order


# Main program 6.


print('Welcome to the tile puzzle. You have to make it so that the numbers are sorted, moiving the tiles in respect to the empty space in the n by n puzzle!')

n = int(input('Enter the desired dimensions of your square tile puzzle: '))

move_count = 0

game_over = False


puzzle = getNewPuzzle(n) 


while not game_over:

    displayBoard(puzzle)

    move = nextMove(puzzle)

    makeMove(puzzle, move)
    
    move_count += 1

    if puzzleWin(puzzle):
        print('Congratulations! You have completed the puzzle! ')
        game_over = True

    elif (n == 9 and move_count >= 31) or (n == 15 and move_count >= 80):
        print('Best of luck next time! ')
        game_over = True
        

    




