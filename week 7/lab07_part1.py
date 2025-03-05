'''
given a dictionary of keys that are strings and/or integers, values are lists, write a snippet of code
that returns total number of elements of all lists that have keys as strings 

example :

d  = {3: [3, 6], 'a': [3, 4, 5], 'b': [7, 8, 91, 1]}


'''

def dict_elements(dict):
    value_count = 0
    for key in dict:
        if type(key) == str:
            value_count += len(dict[key])
    return value_count



'''
write a function wordTally that takes an integer argument n and read n words from the user. Note that
the user may enter the same word multiple times.

Your function should tally up how many times each word occurs that the user has entered and store it in a dictionary where 
the keys are the words and the values are the number of times each word occurs.

return this dictionary.

you may create only one collection, namely the dictionary to be returned.

'''

def wordTally(n):
    words = []
    occurs = {}
    for _ in range(n):
        word = input('Enter a word: ')
        words.append(word)
    
    for word in words:
        occurs[word] = words.count(word)

    return occurs


'''
d = {3: 5, 4: 5, 6: 1}

d_inverted = {5: [3, 4], 1: [6]}

'''

def inverted(d : dict):
    values = list(d.values())
    keys = list(d.keys())

    d_inverted = {}

    for value in values:
        d_inverted[value] = [element for element in keys if d[element] == value]

    return d_inverted
    


'''
cut: 4

fox : 3

hi : 2

bye: 2

river:1

stream: 1

brook: 1

k = 1 wit

k = 2 fox

k = 3 hi, bye

k=4

nothing

k= 5

river, stream

'''






    