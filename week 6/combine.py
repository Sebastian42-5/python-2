def combine(d1, d2):

    '''

    return a new dictionary where each key 
    is a key that is both in d1 and d2

    '''
    new_dict = {}

    for key in d1:
        if key in d2:
            lst_d1 = d1[key]
            lst_d2 = d2[key]
            new_dict[key] = sum(lst_d1) + sum(lst_d2)
    return new_dict


d1 = {1: [2], 4: [5, 6]}

d2 = {4: [8]}


print(combine(d1, d2))