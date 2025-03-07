

# topic 1 : combined 
# question type and difficulty : long answer: medium

# topic 2 : dictionaires
# Question type and difficulty : Short answer: medium 


# topic 1

'''
You and your friend are doing a challenge: you are playing three tic tac toe games combined, put within a dictionary. The X's are 1s and the Os are 2s. 

Also, the keys are strings of the name of the player which won the game (which is a 2d list)

After you finish 25 games of this double tic tac toe, you need to store the number of vertical, horizontal and diagonal wins for each game

You need to generate three random games a) and afterwards, 

use a histogram to represents the vertical wins, the horizontal wins and the diagonal wins with the data show above (b)

c) what is the time complexity of this program?

You have to use list comprehension in this question!

'''

# answer :

import random 

def check_win(board):

    horizontalwins = 0
    verticalwins = 0
    diagonalwins = 0

    player = None

    for row in board:
        if row[0] == row[1] == row[2]: # horizontal win
            horizontalwins += 1
            if row[0] == 1:
                player = 'Player1'
            else:
                player = 'Player2'
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]: # vertical win 
            verticalwins += 1
            if board[0][col] == 1:
                player = 'Player1'
            else:
                player = 'Player2'
    if board[0][0] == board[1][1] == board[2][2]: # front diagonal win
        diagonalwins += 1
        if board[0][0] == 1:
            player = 'Player1'
        else:
            player = 'Player2'
    
    elif board[0][2] == board[1][1] == board[2][0]: # back diagonal win
        diagonalwins += 1
        if board[0][0] == 1:
            player = 'Player1'
        else:
            player = 'Player2'

    return player, horizontalwins, verticalwins, diagonalwins


def create_game():

    games = {'Player1': [], 'Player2': []}

    total_horizontal = 0
    total_vertical = 0
    total_diagonal = 0

    for _ in range(3):
        board = [[random.randint(1, 2) for _ in range(3)] for _ in range(3)]

        winner, h, v, d = check_win(board)

        total_horizontal += h
        total_vertical += v
        total_diagonal += d


        if winner:
            games[winner].append(board)

    return games, total_horizontal, total_vertical, total_diagonal


games = create_game()


print(games)


# topic 2: Failed cooking book

''' 
You want to cook a matcha cheesecake for your mom. However, the cooking book has all of the steps completely reversed and numbered +2.

Fix the cookbook (which is actually a dictionary where the keys are the steps and the values are the step numbers) so you can cook the cheesecake!

You also want a list with the steps for better readability. Dictionaires confused you...

Hurry! Your mom is coming soon!

'''

# answer:

def fixingCookbook(d: dict):

    reversed_dict = dict(reversed(list(d.items())))

    for key in reversed_dict:
        reversed_dict[key] -= 2

    return reversed_dict, list(reversed_dict.keys())

# print(fixingCookbook({'bake': 5, 'cook': 4, 'water': 3}))



