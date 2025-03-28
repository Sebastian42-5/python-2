def happy(n):
    '''
    n = 19 

    returns True, because 

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

    '''

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    

    return n == 1


print(happy(19))