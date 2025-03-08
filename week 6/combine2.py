def combine2(d1, d2):
    '''
    
    >>> combine2({a: {3: [2], 4: [5. 6]}}, {'b': {3:[8, 12]}})

    {3: 22}

    For this problem, you want to combine two dictionairies that contain dictionaires with lists and
    you want to add the elements of the common keys of the two dictionairies. 
    
    '''

    



    # new_dict = {}

    # for dict in d1:
    #     for key in dict:
    #         if key in d2:
    #             lst_d1 = d1[dict][key]
    #             lst_d2 = d2[dict][key]
    #             new_dict[key] = sum(lst_d1) + sum(lst_d2)
    # return new_dict






d1 = {'a': {3: [2], 4: [5, 6]}, 'b': {7: [2, 7, 9], 4: [5, 6]} }

d2 = {'a': {3: [8, 12]}, 'b': {7: [7, 33]}}

print(combine2(d1, d2))



