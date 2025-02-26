from math import factorial

def binom(n, k):
    num = factorial(n) # this is O(n)
    denom = factorial(k) * factorial(n - k) # this is 2 * O(n)

    return num // denom # this is O(n)

print(binom(3, 2))


def pascal_triangle(n):   # space complexity of n^2 (2 dimensional list)
    matrix = []
    for row in range(n): 
        # This algorithm is O(n^3)
        sub_lst = []
        for k in range(row + 1):  
            # this inner loop is n^2 
            sub_lst.append(binom(row, k)) # if we can make this constant, we are good to go
        matrix.append(sub_lst)

    return matrix



def print_pascal(matrix): 
    for row in matrix: # our first loop is going O(n) times # a two dimensional list takes square space n^2
        for i in range(len(row)): # worse case, we have n columns, so this is O(n) times as well 
            print(row[i], end = ''.center(4))
        print()
    

# print_pascal(pascal_triangle(5))


# matrix[row][k]
# matrix[row][k] = matrix[row - 1][k - 1] + matrix[row - 1][k]  4 primitive operations 


def pascal_triangle_2(n):
    matrix = []

    for row in range(n):
        sub_lst = [1]

        if row > 0:
            last_row = matrix[-1]
            for k in range(row - 1):
                sub_lst.append(last_row[k] + last_row[k + 1])
            sub_lst.append(1)

        matrix.append(sub_lst)

    return matrix


# print_pascal(pascal_triangle_2(7))

# printing it all for each row you don't store it in a table, so the store space would be constant 


def pascal_triangle_3(n, current_row = 0, matrix = []):

    if current_row == n:
        return
    if current_row == 0:

        sub_lst = [1]

    else:

        sub_lst = [1]

        last_row = matrix[-1]

        for i in range(len(last_row) - 1):
            sub_lst.append(last_row[i] + last_row[i + 1])
        sub_lst.append(1)

    matrix.append(sub_lst)

    print('  '.join(map(str, sub_lst)).center(n * 4))

    pascal_triangle_3(n, current_row + 1, matrix)



# print_pascal(pascal_triangle_2(7)) 

pascal_triangle_3(8)