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
print(output) 

