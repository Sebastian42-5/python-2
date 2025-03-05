
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


'''




# topic 2: Failed cooking book

''' 
You want to cook a matcha cheesecake for your mother. However, the cooking book has all of the steps completely reversed and numbered +2 instead of normally.

Fix the cookbook (which is actually a dictionary where the keys are the steps and the values are the step numbers) so you can cook the cheesecake!

'''

# answer:

def fixingCookbook(d: dict):

    reversed_dict = dict(reversed(list(d.items())))

    for key in reversed_dict:
        reversed_dict[key] -= 2

    return reversed_dict

print(fixingCookbook({'bake': 5, 'cook': 4, 'water': 3}))



