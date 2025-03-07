
# pandas + numpy + matplotlib

# debugging and error messages

# nested loops (two dimensional lists and complexity)

# tuples

# time space complexity 

# dictionaries 

# we need to come up with two mock questions and submit them by Friday 




# topic 1 : combined 
# question type and difficulty : long answer: medium

# topic 2 : dictionaires
# Question type and difficulty : Short answer: medium 


# topic 1

'''
You and your friend are doing a challenge: you are playing three tic tac toe games combined, put within a dictionary. The X's are 1s and the Os are 2s. 

Also, the keys are strings of the name of the player which originally has the most rows to their name and the values are the tic tac toe game (which is a 2d list)

After you finish 25 games of this double tic tac toe, you have this interesting data:

There was 9 vertical wins, 4 horizontal wins and 12 diagonal wins.

In every game, there is already an 1 or a 2 for each row. 

You need to generate three random games a) and afterwards, 

use a histogram to represents the vertical wins, the horizontal wins and the diagonal wins with the data show above (b)

'''

def tictactoe(dict):
    for value in dict:
        for row in value:



game = {'Player1': [[1],[2],[1]], 'Player2': [[2],[2],[1]], 'Player1': [[1],[1],[2]]} 



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

print(fixingCookbook({'bake': 5, 'cook': 4, 'water': 3}))



