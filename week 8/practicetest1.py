# 6

# def countPeaks(matrix):
#     rows = len(matrix)

#     columns = len(matrix[0])

#     for i in range(rows):
#         for j in range(columns):
#             if matrix[i][j] > matrix[i - 1][j] and matrix[i][j] > matrix[i + 1][j]


# 7 

# 8

# 9

# 10

def countDigits(matrix, n):
    
    digit_count = 0

    rows = len(matrix)

    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            if int(matrix[i][j]) == n:
                digit_count += 1
    return digit_count


# print(countDigits([['1', '1', '2'], ['3', '4', '1']], 1))


# 11

# 12

# 13

def count_frequences(lst: list):
    freq = {}

    for num in lst:
        value = lst.count(num)
        freq.update({num: value})
    
    return freq

# print(count_frequences([1, 1, 2, 2, 2, 3, 3, 3, 3]))


# 14

def process_tuples(tup1, tup2): 
    result = [] 
    for i in range(len(tup1)): 
        result.append(tup1[i] + tup2[i]) 
    return tuple(result) 
 
t1 = (1, 2, 3) 
t2 = (4, 5, 6) 
output = process_tuples(t1, t2) 
# print(output) 


# 17 



def tupleIsEqual(d):
    correct_sum = []
    for key in d:
        if sum(d[key][1]) == d[key][0]:
            correct_sum.append(d[key][1])

    return correct_sum

# print(tupleIsEqual({1: (5, [2, 3]), 2: (4, [4, 5]), 3: (6, [1, 5])}))



# 18

t = ((3, 2, 6), (5, 2, 1), (4, 8)) 
 
def elementsTuple(t: tuple): 
    l = [] 
    for tup in t: 
        for i in range(len(tup)): 
            l.append(tup[i]) 
    l = tuple(sorted(l)) 
    return l 
 
# print(elementsTuple(t)) 
 
 


# 19

lst = [[5, 5, 4],  
       [8, 4, 7],  
       [2, 5, 1]] 
 
def checkSum(lst):  
    sum1 = 0 
    sum2 = 0 
    for i in range(len(lst)): 
        sum1 += lst[i][i] 
        sum2 += lst[i][-1-i] 
    return sum1 == sum2 
 
# print(checkSum(lst))


# 20

# products = {'laptop': 800, 'phone': 600, 'tablet': 400, 'headphones': 150} 
# discounts = {'laptop': 10, 'phone': 5, 'tablet': 20} 
# for product in discounts(): 
#   if product in products: 
#     products[product] = products[product]*(1-discount/100) 
# print(products)


# 21


tuple = (10, 20, 30 , 40) 
lst = list(tuple) 
lst[1] = 'Hello'
# print(tuple) 
# print(lst) 


# 24

def lollipop(matrix):
    pass

# 25

d1 = {3: 5, 4: 5, 1:5, 11:42, 0.5:12} 
d2 = {9: 45, 16:37, 25:1, 11:51, 144:0.25} 
 
output = [] 
for key in d1: 
    if d1[key]**2 in d2 and key == d2[d1[key]**2]: 
        output.append(True) 
    else: 
        output.append(False) 
 
# print(output) 

# 26 

d = {(3,4):12, (4,5):9, (10,10):100, (2,2):4, (10,20):200} 
 
param1 = [] 
for key in d: 
    if key[0] * key[1] == d[key]: 
        param1.append(True) 
    else: 
        param1.append(False) 
 
param2 = [key[0] + key[1] == d[key] for key in d] 
 
output = [param1[i] == param2[i] for i in range(len(param1))] 
 
# for i in range(len(output)): 
#     print(output[i], end=" ") 
 

 
# 28. What is the output of the following snippet of code?  What is the time complexity of the code below?  


a = [[]] 

for i in range(10): 
    if i % 3 == 1: 
        a.append([]) 
        for i in range(3): 
            a[-1].append([i ** 2]) 
    elif i % 2 == 0: 
        a[-1].append(3) 
 
# print(a[1])
   

# 31


lst_of_keys = [3, None, "a", False, 16.0] 
lst = [[3, 5, 16], ["r", "i", "E", "c"], 145, "Computers", None, 1600.45, "yay!"] 
 
def listToDict(lst_of_keys, lst): 
    """ 
Iterates over every key in lst_of_keys, assigning them to the 
value with the matching index in lst. 
    """ 
    temp_dict = {} 

    for i in range(len(lst_of_keys)):
        temp_dict[lst_of_keys[i]] = lst[i]

    return temp_dict


# print(listToDict(lst_of_keys, lst))
 

# 32

d = {'a': 10, 'b': 20, 'c': 30} 
d['d'] = d.get('e', 40) 
# print(d)


# 33

# bug 1 : for student, grades in students 

# bug 2 : top_student == student shouldn't be a double equal 

# bug 3 : it's looping through the keys which are strings and it's trying to add it to the total

# bug 4 : the total should be an outer variable 

students = { 
    'Alice': [85, 90, 78], 
    'Bob': [92, 88, 95], 
    'Charlie': [70, 80, 65], 
    'David': [100, 98, 95] 
} 
 
highest_avg = 0 
top_student = "" 
total = 0
 
for student in students: 

    total = sum(students[student])

    average = total / len(students[student])
 
    if average > highest_avg: 
        highest_avg = average 
        top_student = student 
 

# print(f"The student with the highest average is {top_student} with an average of {highest_avg}.")


# 34 

butterflies = { 'name': 'Monarch',
  'count': 10,  
  'Location': ['forest', 'lake'] } 
 
butterflies['count'] = butterflies.get('count') + 1 
if 'colour' not in butterflies.keys(): 
  butterflies['colour'] = 'orange' 
  butterflies.get('Location', []).append('meadow') 
   
# for key in butterflies: 
#     print(f'{key}: {butterflies[key]}')  


# 37 

matrix = [ [1, 2, 3],  
     [4, 5, 6],  
     [7, 8, 9] ] 


sorted_lst = [vector[v] for v in range(3) for vector in matrix] 

# print(sorted_lst)


#  41 


def words(lst): 
    dict = {} 
 
    for word in lst: 
        l_counts = {} 
        for letter in word: 
            if letter in l_counts: 
                l_counts[letter] += 1 
            else: 
                l_counts[letter] = 1 
 
        m_count = 0 
        max_l = [] 
        for letter, count in l_counts.items(): 
            if count > m_count: 
                m_count = count 
                max_l = [letter] 
            elif count == m_count: 
                max_l.append(letter) 
 
        chosen = max_l[0] 
        for letter in max_l: 
            if letter < chosen: 
                chosen = letter 
 
        if chosen not in dict: 
            dict[chosen] = [] 
        dict[chosen].append(word) 
 
    to_remove = [] 
    for key in dict: 
        count = 0 
        for word in dict[key]: 
            count += 1 
        if count <= 1: 
            to_remove.append(key) 
 
    for key in to_remove: 
        del dict[key] 
 
    new_keys = [] 
    for key in dict: 
        inserted = False 
        for i in range(len(new_keys)): 
            if key < new_keys[i]: 
                new_keys.insert(i, key) 
                inserted = True 
                break 
        if not inserted: 
            new_keys.append(key) 
 
    new_dict = {} 
    for key in new_keys: 
        new_dict[key] = dict[key] 
 
    print(new_dict) 
 
lst = ['big', 'but', 'born', 'alt', 'any', 'little', 'lots', 'bill', 
'almost', 'giraffe', 'fox'] 

# words(lst)


# 42

k = 0 
for i in range(1, 5): 
  k += i ** 3
# print(k)


# 45

matrix = [ [1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9] ]  

total = 0

for i in range(len(matrix)):  
    for j in range(len(matrix[i])):
        if i == j:  
            total += matrix[i][j] * 2  
        else: 
            total -= matrix[i][j]  
# print(total)



# 46 

def modify_tuple(t): 
    x, y, z = t  # here you are referring to each of the three elements of the tuple. You can access those elements with assigning
    new_t = (z, x + y, y - z)  
    return new_t  
 
tuple = ((5, 2, 8), (3, 6, 1), (4, 9, 7))  
lst =  []  
for i in tuple:  
  lst.append(modify_tuple(i))  
 
# print(lst)

# print(lst[1][2] + lst[2][0]) 


# 59 

def flightsData(lst_o_dict : list):
    final_dict = {'total_flights_per_destination': []}

    destination_counts  = {}

    for value in lst_o_dict:
        destination = value['destination']
        flight = value['flights']
        
        if destination in destination_counts:
            destination_counts[destination] += flight
        else:
            destination_counts[destination] = flight
    
    for destination, flight in destination_counts.items():
        final_dict['total_flights_per_destination'].append({'destination': destination, 'flights': flight})



    return final_dict 

lst_o_dict = [ {'destination': 'USA', 'flights': 11}, 
{'destination': 'France', 'flights': 19}, 
{'destination': 'USA', 'flights': 20}, 
{'destination': 'France', 'flights': 10}, 
{'destination': 'Morocco', 'flights': 27}, 
{'destination': 'China', 'flights': 35}, 
{'destination': 'Morocco', 'flights': 9} ]


# print(flightsData(lst_o_dict))


# 66 

def findingWord(matrix, word):

    vertical_join = ''

    for i in range(3):
        if ''.join(matrix[i]) == word:
            return True 
        
        vertical_join += ''.join(matrix[i][0])
        if vertical_join == word:
            return True 
    return False

grid = [  ['r', 'a', 't'], 
['a', 'o', 'g'], 
['c', 'a', 't'] ] 
word = "rat" 

# print(findingWord(grid, word))

# 67 

matrix = [[-1 for _ in range(5)] for _ in range(5)]

# print(matrix)

# this code has a time complexity of O(1) because the number of rows and the number of columns if fixed O(5) * O(25) = O(1)
# otherwise, if it was n rows and n columns, this code would have a time complexity of O(n^2)


# 69 

def modify_tuple(t): 
    t[1][0] += 5   # this is modifying both the list in t1 and the list in t2
    return (t[0] * 2, t[1]) 
 
t1 = (3, [4, 5]) 
t2 = modify_tuple(t1) 
 
# print(t1) 
# print(t2)


# key takeaway: you can modify a pointer inside of a function and if you call this function, it can still modify both the original 
# as well as the pointer





















 

