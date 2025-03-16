'''
write a function called combine2 that takes 2 dictionaires d1 and d2
    and combines them together into a new dictionary and returns
    this dictionary.
Here are the details: 
--> d1 and d2 are dictionary of dictionaries.  The inner dictionary
    values are lists of integers
--> if d1 and d2 have the same key, for which the respective inner
    dictionaries both in d1 and d2 also have the same key k, then
    k is added as a key to the  combined dictionary and the value
    is the sum of the values in the respective lists.  

>>> d1 = {'a': {3: [2], 4: [5, 6]}}
>>> d2 = {'a': {3: [8, 12]}}
>>> combine2(d1, d2)
{3: 22}
'''

def combine2(d1, d2):
    new_dict = {}

    for outer_key in d1:
        if outer_key in d2:
            for inner_key in d1[outer_key]:
                if inner_key in d2[outer_key]:

                    sumd1 = sum(d1[outer_key][inner_key])
                    sumd2 = sum(d2[outer_key][inner_key])

                    new_dict[inner_key] = sumd1 + sumd2
    return new_dict
                

d1 = {'a': {3: [2], 4: [5, 6]}, 'b': {7: [2, 7, 9], 4: [5, 6]} }

d2 = {'a': {3: [8, 12]}, 'b': {7: [7, 33]}}

# print(combine2(d1, d2))


'''
create a file birthdays.py that will do the following:

(a) write a function that reads birthdays of people
    from the user and stores them in a dictionary
    of dictionaries.  Once the user enters 'stop', you 
    will read no more input from the user.  You may
    assume the user will give valid input.

    Sample Input:
    month day name: February 23 Bob
    month day name: May 3 Katie
    month day name: May 8 Paul
    month day name: May 8 Lucy
    month day name: stop

    Sample Ouput (i.e. returned by function)
    { 'February': {'23': ['Bob']},
    'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} }
'''

def birthday_storer():

    birthdays = {}

    stop = False

    while not stop:
        
        birthday = input('month day name: ')

        if birthday == 'stop':
            stop = True
        else:
            parts = birthday.split()

            month = parts[0]
            day = parts[1]
            name = parts[2]

            if month not in birthdays:
                birthdays[month] = {}

            if day not in birthdays[month]:
                birthdays[month][day] = []

            if name not in birthdays[month][day]:
                birthdays[month][day].append(name)

    return birthdays 




'''
(b) Write a function called mostCovered that will take 
the dictionary entered by the user in part (a) and
return the month that has the most number of 
birthdays
'''

def mostCovered(birthdays):

    max_month_count = 0

    for month in birthdays:
        count = len(birthdays[month]) 
        if count > max_month_count:
            max_month_count = count
            max_month = month
    
    return max_month


birthdays = birthday_storer()

# print(mostCovered(birthdays)) 

   

'''
(c) write a function called invert() that will take
the birthday month dictionary entered by the user in
part(a) and return the equivalent birthday dictionary

Sample Input is the dictionary returned in part (a)

Sample Output:
{'Bob': ('February', '23'), 
'Katie': ('May', '3'),
'Paul': ('May', '8'), 
'Lucy': ('May', '8')}
'''

def invert(birthdays):
    new_dict = {}

    for month, days in birthdays.items():
        for day, names in days.items(): 
            for name in names:
                new_dict[name] = (month, day)

    return new_dict
      
      
inverted = invert(birthdays)

print(inverted)

