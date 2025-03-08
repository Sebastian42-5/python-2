def combine2(d1, d2):
    '''
    
    >>> combine2({a: {3: [2], 4: [5, 6]}}, {'b': {3:[8, 12]}})

    {3: 22}

    For this problem, you want to combine two dictionairies that contain dictionaires with lists and
    you want to add the elements of the common keys of the two dictionairies. 
    
    '''


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

print(combine2(d1, d2))



