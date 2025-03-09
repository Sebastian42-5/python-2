# 1

# 2

# 3

# 4

# 5

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
 
print(a[1])
   

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


print(listToDict(lst_of_keys, lst))
 
 
   

