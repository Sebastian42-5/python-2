

# topic 1 : combined 
# question type and difficulty : long answer: medium

# topic 2 : dictionaires
# Question type and difficulty : Short answer: medium 



# topic 1

'''
You and your friend are doing a challenge: you are playing three tic tac toe games combined, put within a dictionary. The X's are 1s and the Os are 2s.

In this tictactoe, there are no order of turns. You and your friends just random put values in the 3 by 3 board spontaneously 

Also, the keys are strings of the name of the player which won the game and the values are the corresponded board in which that player won (which are 2d lists)

After you finish one game of this double tic tac toe, you need to store the number of vertical, horizontal and diagonal wins

You need to generate three random games a) and afterwards, 

use a bar plot to represents the number of vertical wins, horizontal wins and diagonal wins (b)

You have to use list comprehension in this question!

So in the end, your code should print the dictionary, the dataFrame that you create to create the bar plot and the bar plot itself.

Good luck!

'''

# answer : (refer to the .ipynb file)



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



